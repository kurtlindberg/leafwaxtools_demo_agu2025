'''
Map of Lake Qaupat (QPT), Baffin Island, Nunavut, Canada
'''

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature


plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = "Liberation Sans"


projLcc = ccrs.LambertConformal(central_longitude=-70, central_latitude=60)
resol = '50m'
land = cfeature.NaturalEarthFeature(
    'physical', 'land',
    scale=resol, edgecolor='black'
)
border = cfeature.NaturalEarthFeature(
    category='cultural', name='admin_0_boundary_lines_land',
    scale=resol, facecolor='none'
)
ocean = cfeature.NaturalEarthFeature(
    'physical', 'ocean',
    scale=resol, edgecolor='none', facecolor=cfeature.COLORS['water']
)
lakes = cfeature.NaturalEarthFeature(
    'physical', 'lakes',
    scale=resol, edgecolor='none', facecolor=cfeature.COLORS['water']
)

ax = plt.axes(projection=projLcc)
#ax.coastlines(resolution=resol, color='black', zorder=10)
gl = ax.gridlines(
    draw_labels=True, linewidth=1, color='black', alpha=0.5, linestyle='--', zorder=200
)
ax.add_feature(land, facecolor='white', alpha=0.7, zorder=5)
ax.add_feature(border, alpha=1, linewidth=1, zorder=50)
ax.add_feature(ocean, zorder=1)  # facecolor='lightgrey'
#ax.add_feature(lakes, zorder=25)
ax.set_extent([-85, -55, 56, 75], crs=ccrs.PlateCarree())

ax.plot(
  [
    -68.20
  ],
  [
    63.68
  ],
  'd', color='yellow', markeredgecolor='k', markersize=12,
  zorder=100, transform=ccrs.PlateCarree()
)

figure_qpt_map = plt.gcf()
# figure_qpt_map.savefig("figures/qpt_fig_map.svg", dpi=300)
