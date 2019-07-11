![header](https://zupimages.net/up/19/28/16vk.bmp)

# Astronomy data visualization Milky Way and integration radio astronomy Pulsar data

## Presentation

##### __Script 1 :__ Galaxy tour
this script shows us all the planets presents in the solar system
[![script1](https://zupimages.net/up/19/28/vlrl.bmp)](https://www.youtube.com/watch?v=hJ8n_CsV6h8)

##### __Script 2 :__ Orbit overview
this script shows us planets orbit,and how it representation change while the focused planet change
[![script2](https://zupimages.net/up/19/28/3n23.bmp)](https://www.youtube.com/watch?v=HXVy8NHdVxs)

##### __Script 3 :__ Gaia Sky visual effects
this script shows us some visual effects on gaia sky software
[![script3](https://zupimages.net/up/19/28/ir8v.bmp)](https://www.youtube.com/watch?v=ND1Y06MIAf8&feature=youtu.be)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
What things you need to install the software and how to install them.
A number of prequisites need to be considered:

Operating system Linux / Windows 7+ / macOS/ Virtualbox environment  
CPU Intel Core i5 3rd Generation or similar  
GPU Intel HD 4000, Nvidia GeForce 9800 GT, Radeon HD 5670 / 1 GB VRAM / OpenGL 3.0  
Memory 4+ GB RAM  
Hard drive 1 GB of free disk space  

### Installing

One can install the Gaia Sky program with the following link: https://gaia-sky.readthedocs.io/en/latest/Downloads.html#
The scripts and showcases can be found here: https://gitlab.com/langurmonkey/gaiasky/tree/master/assets/scripts

#### Installation on Windows

To download the installer depending on your architecture (32 or 64 bits), select the good one following this link: https://zah.uni-heidelberg.de/institutes/ari/gaia/outreach/gaiasky/downloads/ 
You just have to follow instructions of the graphical interface.

#### Instalation on Debian based systems (Linux)

Download the installer script with this command

` wget http://gaia.ari.uni-heidelberg.de/gaiasky/files/releases/2.1.7.a67779dc/gaiasky_unix_2_1_7_a67779dc.sh`

Then run the script and follow the installer instructions

` sh ./gaiasky_unix_2_1_7_a67779dc.sh`

#### Installation on Mac OS

For macOS Gaia Sky provides a gaiasky_macos_<version>.dmg file below  

https://zah.uni-heidelberg.de/institutes/ari/gaia/outreach/gaiasky/downloads/
  
It is is installed by unpacking into theApplications folder. Once unpacked, it is ready to run by simply clicking on it.  

## Scripts 

In order to run Python scripts, click on the Run script button (the little car) at the bottom of the GUI window. A new
window will pop up allowing you to select the script you want to run. Once you have selected it, press run. The script will be
checked for errors. If no errors were found, you will be notified in the box below and you’ll be able to run the script
right away by clicking on the Run button. If the script contains errors, you will be notified in the box below and you
will not be able to run the script until these errors are dealt with.
The scripts are in Python.

For macOs, the scripts are in the following path :
` /Applications/Gaia Sky.app/Contents/java/app/scripts/tests`

## The coordinate system explained 
The coordinate system used in Gaia Sky is the galactic coordinate system. In this celestial coordinate system, the Sun is at its center.In this coordinate system, the primary is aligned with the center of the Milky Way and the fundamental plane parallel to an approximation of the galactic plane but offset to its north.The convention used is the right-handed convention.
Galactic Latitude: it is like the Earth's Equator, so it is at 0° latitude
Galactic Longitude: galactic coordinates go from 0 to 360°.

<!--

The earth's center is used as reference object when locating other celestial bodies. This locating is done by using two variables. The first being right ascension and the second being declination.

The right ascension (α) is the coordinate from the equatorial coordinate system in the sky that has the same role as the longitude in other coordinate systems. The right ascension is usually measured not in degrees as the other longitudes are, but rather in units of time, such that 360 degrees correspond to 24 hours of right ascension.

The declination (δ) in astronomy is comparable to geographic latitude, projected onto the celestial sphere.
It basically means how far above or below the celestial equator. Points north of the celestial equator have positive declinations, while those south have negative declinations. It is customarily measured in the degrees ( ° ) with 90° equivalent to a quarter circle.

When both are combined, these astronomical coordinates specify the direction of a point on the celestial sphere in the equatorial coordinate system" -->
## Data in Gaia Sky
Gaia Sky software uses data from Gaia space sensor.
These data are stored in a [ADQL](http://gea.esac.esa.int/archive-help/index.html) [database](https://gea.esac.esa.int/archive/) , which is a [SQL](https://www.w3schools.com/sql/) based query language

#### FIg1: ADQL Query to get Earth data from database
```sql
SELECT TOP 500 *
FROM gaiadr2.gaia_source 
WHERE CONTAINS(POINT('ICRS',gaiadr2.gaia_source.ra,gaiadr2.gaia_source.dec),CIRCLE('ICRS',252.779,-22.495,0.001388888888888889))=1
```

The database store pre-processed data from Gaia space mission 
#### Fig2: Earth data in Gaia's database

| solution_id         | designation                  | source_id           | random_index | ref_epoch | ra                 | ra_error           | dec                 | dec_error          | parallax | parallax_error | parallax_over_error | pmra | pmra_error | pmdec | pmdec_error | ra_dec_corr | ra_parallax_corr | ra_pmra_corr | ra_pmdec_corr | dec_parallax_corr | dec_pmra_corr | dec_pmdec_corr | parallax_pmra_corr | parallax_pmdec_corr | pmra_pmdec_corr | astrometric_n_obs_al | astrometric_n_obs_ac | astrometric_n_good_obs_al | astrometric_n_bad_obs_al | astrometric_gof_al | astrometric_chi2_al | astrometric_excess_noise | astrometric_excess_noise_sig | astrometric_params_solved | astrometric_primary_flag | astrometric_weight_al | astrometric_pseudo_colour | astrometric_pseudo_colour_error | mean_varpi_factor_al | astrometric_matched_observations | visibility_periods_used | astrometric_sigma5d_max | frame_rotator_object_type | matched_observations | duplicated_source | phot_g_n_obs | phot_g_mean_flux  | phot_g_mean_flux_error | phot_g_mean_flux_over_error | phot_g_mean_mag | phot_bp_n_obs | phot_bp_mean_flux | phot_bp_mean_flux_error | phot_bp_mean_flux_over_error | phot_bp_mean_mag | phot_rp_n_obs | phot_rp_mean_flux  | phot_rp_mean_flux_error | phot_rp_mean_flux_over_error | phot_rp_mean_mag | phot_bp_rp_excess_factor | phot_proc_mode | bp_rp     | bp_g       | g_rp      | radial_velocity | radial_velocity_error | rv_nb_transits | rv_template_teff | rv_template_logg | rv_template_fe_h | phot_variable_flag | l                 | b                  | ecl_lon            | ecl_lat              | priam_flags | teff_val | teff_percentile_lower | teff_percentile_upper | a_g_val | a_g_percentile_lower | a_g_percentile_upper | e_bp_min_rp_val | e_bp_min_rp_percentile_lower | e_bp_min_rp_percentile_upper | flame_flags | radius_val | radius_percentile_lower | radius_percentile_upper | lum_val | lum_percentile_lower | lum_percentile_upper | datalink_url                                                                  | epoch_photometry_url |
|---------------------|------------------------------|---------------------|--------------|-----------|--------------------|--------------------|---------------------|--------------------|----------|----------------|---------------------|------|------------|-------|-------------|-------------|------------------|--------------|---------------|-------------------|---------------|----------------|--------------------|---------------------|-----------------|----------------------|----------------------|---------------------------|--------------------------|--------------------|---------------------|--------------------------|------------------------------|---------------------------|--------------------------|-----------------------|---------------------------|---------------------------------|----------------------|----------------------------------|-------------------------|-------------------------|---------------------------|----------------------|-------------------|--------------|-------------------|------------------------|-----------------------------|-----------------|---------------|-------------------|-------------------------|------------------------------|------------------|---------------|--------------------|-------------------------|------------------------------|------------------|--------------------------|----------------|-----------|------------|-----------|-----------------|-----------------------|----------------|------------------|------------------|------------------|--------------------|-------------------|--------------------|--------------------|----------------------|-------------|----------|-----------------------|-----------------------|---------|----------------------|----------------------|-----------------|------------------------------|------------------------------|-------------|------------|-------------------------|-------------------------|---------|----------------------|----------------------|-------------------------------------------------------------------------------|----------------------|
| 1635721458409799680 | Gaia DR2 4125822829532278272 | 4125822829532278272 | 1600099805   | 2015.5    | 252.77937134039195 | 3.9160121182413254 | -22.494637735804137 | 1.7495751894073581 |          |                |                     |      |            |       |             | 0.117518395 |                  |              |               |                   |               |                |                    |                     |                 | 147                  | 0                    | 145                       | 2                        | 2.0251923          | 175.9183            | 0.0                      | 0.0                          | 3                         | false                    | 0.016501904           |                           |                                 | 0.117749624          | 17                               | 7                       | 6.6107693               | 0                         | 17                   | false             | 147          | 92.90657195063832 | 1.0685977026958142     | 86.94251                    | 20.76825        | 15            | 52.8415101386992  | 12.783109564327964      | 4.1336975                    | 21.043951        | 14            | 105.08394048720486 | 10.589616068984055      | 9.923301                     | 19.708078        | 1.6998308                | 0              | 1.3358727 | 0.27570152 | 1.0601711 |                 |                       | 0              |                  |                  |                  | NOT_AVAILABLE      | 358.3254924022692 | 13.749301875427319 | 254.12576459398673 | 6.596915387961713E-4 |             |          |                       |                       |         |                      |                      |                 |                              |                              |             |            |                         |                         |         |                      |                      | http://geadata.esac.esa.int/data-server/datalink/links?ID=4125822829532278272 |                      |


But the Gaia Sky software can't use them directly. That's why processed data are used.
These data are stored in Json or Csv files with a structure that could be use by the software

#### Fig3: Earth data in Json dataset

```json
{
	"name" : "Earth",
	"wikiname" :"Earth",
	"color" : [0.13, 0.26, 0.89, 1.0],
	"size" : 6371.1,
	"ct" : "Planets",

	"absmag" : -2.78,
	"appmag" : -3.1,
	
	"parent" : "Sol", 
	"impl" : "gaia.cu9.ari.gaiaorbit.scenegraph.Planet",
	"refplane" : "ecliptic",
	
	"locvamultiplier" : 3.0,
	"locthoverfactor" : 8.0,
	
	"coordinates" : {
		        "impl" : "gaia.cu9.ari.gaiaorbit.util.coord.vsop87.EarthVSOP87",
						"orbitname" : "Earth orbit"
					},	
		
	"rotation" 		: {
						"period" : 23.93447117,
						"axialtilt" : -23.4392911,
						"inclination" : 0.0,
						"meridianangle" : 180.0
						},
						
	"model"			: {
						"args" : [true],
						"type" : "sphere",
						"params" : {
									"quality" : 180,
									"diameter" : 1.0,
									"flip" : false
									},
						"texture" : {
									"base" : "data/tex/base/earth-day*.jpg",
									"specular" : "data/tex/base/earth-specular*.jpg",
									"normal" : "data/tex/base/earth-normal*.jpg",
									"night" : "data/tex/base/earth-night*.jpg",
									}
						},
						
	"cloud"         : {
						"size" : 6390.0,
						"cloud" : "data/tex/base/earth-cloud.jpg",

						"params" : {
									"quality" : 180,
									"diameter" : 2.0,
									"flip" : false
									}
					},
									
	"atmosphere" 	: {
						"size" : 6450.0,
						"wavelengths" : [0.65, 0.57, 0.475],
						"m_Kr" : 0.0025,
						"m_Km" : 0.0015,
						"correctground" : true,
						
						"params" : {
									"quality" : 180,
									"diameter" : 2.0,
									"flip" : true
									}
						}
	}
```

Datasets are usually stored , and loaded in this way

![data](https://zupimages.net/up/19/28/4r1q.png)

## Used tool

This is the list of all used tool used in this course

* [PyCharm](https://www.jetbrains.com/pycharm/?fromMenu) - JetBrain's Python IDE
* [Intellij Idea](https://www.jetbrains.com/idea/?fromMenu) - JetBrain's Java IDE
* [Xcode](https://developer.apple.com/xcode/) - IOs IDE
* [Trello](https://trello.com/b/nOPd1jMy/sprint-1) - Online Kanban tool
* [Discord](https://discordapp.com/) - Online chat application

## Authors

* **Kevin OGIER** - [GitHub](https://github.com/KevinOGIER)
* **Céline MARIN** - [GitHub](https://github.com/GeekyGodess)
* **Kostis Thanos** - [GitHub](https://github.com/kostis95)
* **Nicolas LEFEBVRE** - [GitHub](https://github.com/kyuno053) 
* **HyunJun Moon** - [GitHub](https://github.com/mthekid)
