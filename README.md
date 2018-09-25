# Weather Report App

This is a single page application featuring global map and having the functionalities of displaying **Weather Report** of added locations(markers).

1.  ## How to Access

    *   ### **Domain Name:**

        [shubham151403.pythonanywhere.com](http://shubham151403.pythonanywhere.com)
    *   ### **Description:**

        *   ### Hover over the marker

            Upon **hover** it will popup the <srong>Latitude & Longitude</srong> of the marker location.

        *   ### Click Marker

            Upon **click** it will<srong>Zoom In</srong> to the marker location and shows the **Current Weather Report** of clicked marker location.

        *   ### Further Click On The Marker

            Upon **Further Click** it will<srong>Zoom Out</srong> from marker location to normal view.

        *   ### Click On The **Add location** Button

            Upon Click**Add Lcocation** a <srong>Form</srong> Having the fields namely **Name, Latitude, Longitude**

        *   ### Submit Button

            Upon Click**Submit** Button, the data will be send to the **Backend Server** after **Validation** check. If **Error** occured it will shows the error.

2.  ## Web App Details

    1.  ### Weather Report

        *   Shows **current weather conditon** of clicked location.
        *   Shows **Wind Speed** of clicked location.
        *   Shows **Humidity** of clicked location.
        *   Shows **Temperature(°F)** of clicked location.
        *   Shows **Summary** of clicked location.
    2.  ### Add Location

        *   **Required <sup>*</sup>** Form Fields
            *   **Name** of the desired locaton.
            *   **Latitude** of the desired locaton.
            *   **Longitude** of the desired locaton.
            *   **Submit**(Button) Click/Touch
    3.  ### Development Details

        1.  ## **Technologies Used**

            *   ### **Front End**

            *   #### **Languages/Technologies**

            *   HTML5
            *   CSS3
            *   JavaScript(ECMAScript 5-6)
            *   Python3
            *   AJAX

            *   #### **Front End Libraries**

            *   Jquery
            *   Leaflet
            *   Mapbox

            *   ### **Back End**

                *   Django Web Framework
                *   SQLite3 Database
            *   ### **Third Party Application Programming Interface**

                *   Dark Sky Web API
                *   FourSquare Web API
                *   MapBox maop API
        2.  ## **Web App Deployment (Pythonfromanywhere.com)**

            *   ### Brief Details

                Deploying a Django project on PythonAnywhere is a lot like running a Django project on your own PC. You'll use a virtualenv, just like you probably do on your own PC, you'll have a copy of your code on PythonAnywhere which you can edit and browse and commit to version control.

            *   ### Procedure

                *   ### Commands

                *   `git clone https://github.com/subhmmisra/Wheather_App.git`
                *   `mkvirtualenv --python=/usr/bin/python3.4 mysite-virtualenv`
                *   `(mysite-virtualenv)$ pip install django`

                *   ### Setting up your Web app and WSGI file

                    *   The path to your Django project's top folder -- the folder that contains "manage.py", eg /home/myusername/mysite
                    *   The name of your project (that's the name of the folder that contains your settings.py), eg mysite
                    *   The name of your virtualenv, eg mysite-virtualenv
                *   ### Edit WSGI file

                    *   Edit WSGI according to the requirements
        3.  ## Future Scopes

            *   ### Features

                *   ### Responsiveness

                    *   Media Queries
                    *   Srcset (Responsive Images)
                    *   CSS3 grid
                    *   Viewport Related Unites (vh&vw)
                *   ### Web Securities

                    *   OAuth2 (Third Party Api Protection)
                    *   Registration & Login
                        *   Password Hashing
                        *   Password Salting
                        *   Third Party Login using OAuth2
                    *   RESTFull Web APIs
                        *   API Endpoints
                        *   API Endpoints Security
                    *   Producton Database
                        *   PostgreSQL
                    *   Deployment
                        *   Production server (AWS lightsail)
                        *   Private & Public Key Protection
                        *   Firewall Configuration
                *   **Functionalities**
                    *   **HTTP2**
                    *   **C R U D** Functionality
                    *   Provision of **API** Endpoints
                    *   **Progressive** Web App
        4.  **References**
            *   [https://www.youtube.com/watch?v=wIRVn2dZkaA](https://www.youtube.com/watch?v=wIRVn2dZkaA)
            *   [https://docs.djangoproject.com/en/2.1/](https://docs.djangoproject.com/en/2.1/)
            *   [https://darksky.net/dev](https://darksky.net/dev)
            *   [https://foursquare.com/](https://foursquare.com/)
