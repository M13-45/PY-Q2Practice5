from pyscript import document, display

def check_country(e):
    country = {
        "ph" : "Philippines",
        "au" : "Australia",
        "jp" : "Japan",
        "fr" : "France",
        "gr" : "Germany",
    }

    country_code = document.getElementById("countries").value

    country["ca"] = "Canada"

    display(country.get(country_code, "Country code not found"), target="output1")