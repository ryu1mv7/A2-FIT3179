import pandas as pd, json, urllib.request

df = pd.read_csv("table_1_1_nom_latest_formal_v2.csv")
world = json.load(urllib.request.urlopen("ne_110m_admin_0_countries.topojson"))
names = [f["properties"]["NAME"] for f in world["objects"]["ne_110m_admin_0_countries"]["geometries"]]
set(names) - set(df["Country"])
