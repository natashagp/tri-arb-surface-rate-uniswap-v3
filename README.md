# Surface Rate Triangular Arbitrage in Uniswap V3

### Step 1

```shell
git clone https://github.com/natashagp/tri-arb-surface-rate-uniswap-v3.git
```

### Step 2

Change to directory tri-arb-surface-rate-uniswap-v3

```shell
cd tri-arb-surface-rate-uniswap-v3
```

### Step 3

Install required packages to run this project

```shell
pip install -r requirements.txt
```

### Step 3

Configure your own ```.env``` file, as shown in the ```.env.example``` file.
Create a ```.env``` file and add your ```API_KEY``` to be able to run this project.
To create your ```API_KEY``` go to [The Graph](https://thegraph.com/studio/apikeys/), connect your Metamask wallet and create an API Key.

### Step 4

Run this project

```shell
python main.py
```

A Json file called ```uniswap_surface_rates.json``` will be created if any surface rate triangular arbitrage opportunity is found.
