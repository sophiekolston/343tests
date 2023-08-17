import sqlalchemy
from sqlalchemy import create_engine
import geopandas as gpd
from shapely.geometry import Point

engine = create_engine('postgresql://postgres:postgres@localhost/skol629')

con = engine.connect()

gdf = gpd.GeoDataFrame({'name': ['uoa general library'], 'geometry': [Point(-36.8512, 174.7692)]}, crs=4326)

#con.execute('CREATE EXTENSION postgis;')
con.execute('DROP TABLE IF EXISTS library')
gdf.to_postgis('library', con)

gdf_sql = gpd.GeoDataFrame.from_postgis('library', con, geom_col='geometry')

gdf_sql