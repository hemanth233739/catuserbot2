from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 8785365
    API_HASH = "48c1934c1df9da5b218cfc1382be1bdf"
    # the name to display in your alive message
    ALIVE_NAME = "Yaaro Oruthan"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "Your value"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "BQCGDdUATyw-qX_T22xrw1Q_tJbMrcOheKS_Qc-dYe4RINWGs5ruvkRG9s01tvOJCRle9IaskG1LDptTsDeCOsZWfWp-t8vpOe0K3_8mA9Xo9r421oK0OB77ahw012uELpc_f8psP7dVKdOzm-3M0pSIFGE2GMEIX_P-sqjXyykhvuwRxLiqkk9x3Y9wjQiNVXrJQ1CER4jxD5wjkILB_pk2xuG6avP2svZApjaoETaG8AeGnezmgyAe5ibO5_JqYBuk7OlfBk1bteajO0nCvZFsjZfdEx2N52fx7X8jZkhnVUaen-4dT92HeDLmoq6pkwatldXUzTQMSgu9IESfIeManUb2ugAAAAFDAnVeAA"
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "7800754581:AAHz7xVzCaNoMRv_F1Xu6G_xAXBO4dTZ5yA"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1002386817181
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"
