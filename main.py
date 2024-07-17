from dotenv import load_dotenv
import os
import requests
import json
import func_triangular_arb

load_dotenv()
api_key = os.getenv("API_KEY")

""" RETRIEVE GRAPH QL MID PRICES FOR UNISWAP """
def retrieve_uniswap_information():
    query = """
        {
          pools(orderBy: totalValueLockedETH, 
            orderDirection: desc, 
            first: 500) 
            {
                id
                totalValueLockedETH
                token0Price
                token1Price
                feeTier
                token0 {id symbol name decimals}
                token1 {id symbol name decimals}
            }
        }
    """

    url = f"https://gateway-arbitrum.network.thegraph.com/api/{api_key}/subgraphs/id/5zvR82QoaXYFyDEKLZ9t6v9adgnptxYpKpSbxtgVENFV"
    req = requests.post(url, json={"query": query})
    json_dict = json.loads(req.text)
    return json_dict


if __name__ == "__main__":
    print("Retrieving Uniswap V3 information with GraphQL")
    pairs = retrieve_uniswap_information()["data"]["pools"]
    print("Structuring pairs for triangular arbitrage")
    structured_pairs = func_triangular_arb.structure_trading_pairs(pairs, limit=500)

    # Get surface rates
    print("Getting surface rates for triangular arbitrage")
    surface_rates_list = []
    for t_pair in structured_pairs:
        surface_rate = func_triangular_arb.calc_triangular_arb_surface_rate(t_pair, min_rate=1.5, amount_in=10)
        if len(surface_rate) > 0:
            surface_rates_list.append(surface_rate)

    # Save to JSON file
    if len(surface_rates_list) > 0:
        with open("uniswap_surface_rates.json", "w") as fp:
            json.dump(surface_rates_list, fp)
            print("File saved.")
    else:
        print("No opportunity found.")
