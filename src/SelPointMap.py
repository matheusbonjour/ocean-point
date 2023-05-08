import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import cartopy.mpl.ticker as cticker
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import xarray as xr
import cmocean.cm as cmo
from matplotlib.patches import Patch, Rectangle
import os

class SelPointMap:
    def __init__(self, dataset_path, region):
        self.dataset_path = dataset_path
        self.region = region
        self.click_count = 0
        self.coords = []

        self.create_map()

    def onclick(self, event):
        self.click_count += 1
        lon, lat = event.xdata, event.ydata
        self.coords.append((lon, lat))
        self.ax.plot(lon, lat, marker='o', markersize=10, color='red', alpha=0.7, markeredgecolor='white', markeredgewidth=2, transform=ccrs.PlateCarree())

        # Adicionar texto "Ponto selecionado" abaixo do ponto
        self.ax.text(lon, lat - 0.5, 'Ponto selecionado', fontsize=12,fontweight='bold', ha='center', va='top', color='black', transform=ccrs.PlateCarree())


        self.fig.canvas.draw()

        file = f'sel_point_{self.region}.png'
        if file in os.listdir('../figures/'):
            os.remove('../figures/' + file)
        plt.savefig(f'../figures/{file}', dpi=300, bbox_inches='tight')
        plt.close()

    def create_map(self):
        ds = xr.open_dataset(self.dataset_path)

        batimetria = ds["z"]

        if self.region == 'sudeste':
            lon_min, lon_max = -50, -36
            lat_min, lat_max = -32, -15
        elif self.region == 'sul':
            lon_min, lon_max = -60, -45
            lat_min, lat_max = -40, -20
        elif self.region == 'nordeste':
            lon_min, lon_max = -45, -30
            lat_min, lat_max = -20, 5

        batimetria_recortada = batimetria.sel(x=slice(lon_min, lon_max), y=slice(lat_min, lat_max))

        self.fig = plt.figure(figsize=(10, 10))
        self.ax = self.fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
        self.ax.set_extent([lon_min, lon_max, lat_min, lat_max], crs=ccrs.PlateCarree())

        gl = self.ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
        gl.top_labels = False
        gl.right_labels = False
        gl.xformatter = cticker.LongitudeFormatter()
        gl.yformatter = cticker.LatitudeFormatter()

        batimetria_recortada = batimetria_recortada * -1
        levels = np.arange(0, 5500, 100)

        cf = self.ax.contourf(batimetria_recortada.x, batimetria_recortada.y, batimetria_recortada, levels=levels, cmap=cmo.deep, transform=ccrs.PlateCarree(), vmin=0, vmax=5000)
        colorbar = plt.colorbar(cf, orientation='horizontal', pad=0.05, shrink=0.8)
        profundidade = colorbar.ax.set_xlabel('Profundidade (m)', fontsize=15)

        resol = '10m'

        self.ax.add_feature(cfeature.NaturalEarthFeature('physical', 'land', scale=resol, edgecolor='k', facecolor=cfeature.COLORS['land']))
        self.ax.add_feature(cfeature.NaturalEarthFeature(category='cultural', name='admin_0_boundary_lines_land', scale=resol, facecolor='none', alpha=0.7))

        self.ax.set_xlabel("Longitude")
        self.ax.set_ylabel("Latitude")

        cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        plt.show()

    
    def get_lat_lon(self):
        return self.coords


# Definir o diretório de trabalho
dataset_path = "../data/ETOPO1_Bed_g_gmt4.grd"

region = input("Escolha uma região: ['nordeste','sudeste','sul'] \nMinha região é: ")

# Executar função
mapa = SelPointMap(dataset_path, region)

coords = mapa.get_lat_lon()
