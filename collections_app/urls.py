from collections_app import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^(?P<collection_id>[0-9]+)/$', views.collection_detail, name='collection_detail'),
    path('rss/', views.LatestEntriesFeed()),
    path('browse/all/', views.browse_all_collections, name='browse_collections_all'),
    path('browse/consortia/', views.browse_consortial_collections, name='browse_collections_consortia'),
    path('browse/digital_collections/', views.browse_digital_collections,
         name='browse_collections_digital'),
    path('browse/locations/', views.locations_list, name='browse_collections_locations'),
    path('browse/location/city/<int:pk>/', views.location_city_collections, name='browse_collections_location_city'),
    path('browse/location/state_prov/<int:pk>/', views.location_state_prov_collections,
         name='browse_collections_location_state_prov'),
    path('browse/location/country/<int:pk>/', views.location_country_collections,
         name='browse_collections_location_country'),
    path('browse/subjects/', views.subjects_list, name='browse_collections_subjects'),
    path('browse/subject/name/<int:pk>', views.subject_name_collections,
         name='browse_collections_subject_name'),
    path('browse/subject/topic/<int:pk>', views.subject_topic_collections,
         name='browse_collections_subject_topic'),
    path('browse/subject/city/<int:pk>', views.subject_city_collections,
         name='browse_collections_subject_city'),
    path('browse/subject/county/<int:pk>', views.subject_county_collections,
         name='browse_collections_subject_county'),
    path('browse/subject/state_prov/<int:pk>', views.subject_state_prov_collections,
         name='browse_collections_subject_state_prov'),
    path('browse/subject/country/<int:pk>', views.subject_country_collections,
         name='browse_collections_subject_country'),
    path('browse/subject/geo_area/<int:pk>', views.subject_geo_area_collections,
         name='browse_collections_subject_geo_area'),
    path('browse/tech_data/', views.tech_data_list, name='browse_collections_tech_data'),
    path('browse/tech_data/spec_format/<int:pk>', views.spec_format_collections,
         name='browse_collections_tech_data_spec_format'),
    path('browse/tech_data/cat_system/<int:pk>', views.cat_system_collections,
         name='browse_collections_tech_data_cat_system'),
    path('random/', views.random_collection),
    path('new/', views.new_collections),
    path('add_collection/', views.add_collection, name='add_collection'),
    path('update/<int:pk>', views.update_collection, name='update-collection'),
    path('delete/<int:pk>', views.delete_collection, name='delete-collection'),
    path('image_add/', views.image_add, name='image_add'),
    path('image_delete/<int:pk>', views.image_delete, name='image_delete'),
    path('image_update/<int:pk>', views.image_update, name='image_update'),
    path('add_document/', views.add_document, name='add_document'),
    path('reference_services/', views.reference_services_list, name='reference_services'),
    path('reference_service_update/<int:pk>/', views.reference_service_update,
         name='reference_service_update'),
    path('reference_service_add/', views.reference_service_add, name='reference_service_add'),
    path('cataloging_systems/', views.cataloging_systems_list, name='cataloging_systems'),
    path('cataloging_system_update/<int:pk>/', views.cataloging_system_update,
         name='cataloging_system_update'),
    path('cataloging_system_add/', views.cataloging_system_add,
         name='cataloging_system_add'),
    path('special_formats/', views.special_formats_list, name='special_formats'),
    path('special_format_update/<int:pk>/', views.special_format_update,
         name='special_format_update'),
    path('special_format_add/', views.special_format_add,
         name='special_format_add'),
    path('subject_names/', views.subjects_names_list, name='subjects_names'),
    path('subject_name_update/<int:pk>/', views.subject_name_update, name='subject_name_update'),
    path('subject_name_add/', views.subject_name_add, name='subject_name_add'),
    path('subject_topics/', views.subjects_topics_list, name='subjects_topics'),
    path('subject_topic_update/<int:pk>/', views.subject_topic_update, name='subject_topic_update'),
    path('subject_topic_add/', views.subject_topic_add, name='subject_topic_add'),
    path('subject_cities/', views.subjects_cities_list, name='subjects_cities'),
    path('subject_city_update/<int:pk>/', views.subject_city_update, name='subject_city_update'),
    path('subject_city_add/', views.subject_city_add, name='subject_city_add'),
    path('subject_counties/', views.subjects_counties_list, name='subjects_counties'),
    path('subject_county_update/<int:pk>/', views.subject_county_update, name='subject_county_update'),
    path('subject_county_add/', views.subject_county_add, name='subject_county_add'),
    path('subject_states_provinces/', views.subjects_states_provinces_list,
         name='subjects_states_provinces'),
    path('subject_state_province_update/<int:pk>/', views.subject_state_province_update,
         name='subject_state_province_update'),
    path('subject_state_province_add/', views.subject_state_province_add,
         name='subject_state_province_add'),
    path('subject_countries/', views.subject_countries_list, name='subjects_countries'),
    path('subject_country_update/<int:pk>/', views.subject_country_update, name='subject_country_update'),
    path('subject_country_add/', views.subject_country_add, name='subject_country_add'),
    path('subject_geo_areas/', views.subject_geo_areas_list, name='subjects_geo_areas'),
    path('subject_geo_area_update/<int:pk>/', views.subject_geo_area_update,
         name='subject_geo_area_update'),
    path('subject_geo_area_add/', views.subject_geo_area_add, name='subject_geo_area_add'),
]