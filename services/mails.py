def mail_message(code):
    return '''

   <!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible"
              content="IE=edge">
        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>

    <body style='background-color:azure;padding:10px;'>

        <p
           style='margin:auto;padding:10px;font-weight:bold;text-align: center; text-transform:uppercase;'>
            BEENANCE </p>

        <br>

        <p class=''
           style='color:black;opacity:0.85;font-size: 100%;text-align:left;font-weight:700;margin:auto;margin-top:15px;margin-bottom: 15px;padding:10px;'>
            Hello! Your email
            address was used to
            create an acccount on our platform,
            please verify
            your account using the code below</p>


        <br>
        <p style="margin:auto;font-size:130%;font-weight: bold;text-align: center;padding:20px;">''' + code + '''
        </p>

        <br>
        <br>
        <p style='font-size:85%;text-align:left;'> Best regards, The Beenance team.</p>




    </body>

</html>


   '''
