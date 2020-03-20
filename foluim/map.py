<<<<<<< HEAD
# !pip install folium

import folium

# Create map object
# > Set the center using 'location' then the zoom
m = folium.Map(location=[25.2709276,55.3207738], zoom_start=11)

# Global tooltip
tooltip = 'Click For More Info'

# Create markers
folium.Marker([25.1977651,55.2794132],
                popup='<strong>Dubai Mall</strong>',
                tooltip=tooltip).add_to(m)

folium.Marker([25.1977651,55.2794132],
                popup='<strong>Dubai Mall</strong>',
                tooltip=tooltip).add_to(m)




# Generate map (HTML)
m.save('map.html')



=======
# !pip install folium

import folium

# Create map object
# > Set the center using 'location' then the zoom
m = folium.Map(location=[25.2709276,55.3207738], zoom_start=11)

# Global tooltip
tooltip = 'Click For More Info'

# Create markers
folium.Marker([25.1977651,55.2794132],
                popup='<strong>Dubai Mall</strong>',
                tooltip=tooltip).add_to(m)

folium.Marker([25.1977651,55.2794132],
                popup='<strong>Dubai Mall</strong>',
                tooltip=tooltip).add_to(m)




# Generate map (HTML)
m.save('map.html')



>>>>>>> connect commit
