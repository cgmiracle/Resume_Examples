import email_apis
import datetime
import smtplib
import ssl
from email.message import EmailMessage

class DailyEmail():

    def __init__(self):
        self.content = {'weather' : {'include' : True, 'content' : email_apis.get_weather()},
                        'scores' : {'include' : True, 'content' : email_apis.get_scores()},
                        'headlines' : {'include' : True, 'content' : email_apis.get_headlines()},
                        'word' : {'include' : True, 'content' : email_apis.get_word_of_day()}
                        }

        self.recipients = ['ENTER EMAIL RECIPIENT']

        self.sender = {'email' : 'SENDER EMAIL',
                       'password' : 'SENDER PASSWORD'}

    def send_email(self):
        #Builds the email message
        msg = EmailMessage()
        msg['Subject'] = f'Daily Update - {datetime.date.today().strftime("%d %b %Y")}'
        msg['From'] = self.sender['email']
        msg['To'] = ', '.join(self.recipients)

        #Adds the plaintext and html contents
        msg_body = self.format_email()
        msg.set_content(msg_body['text'])
        msg.add_alternative(msg_body['html'], subtype='html')

        #Send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smpt.gmail.com', 465, context=context) as server:
            server.login(self.sender['email'],
                         self.sender['password'])
            server.send_message(msg)



    def format_email(self):
        #First generate plaintext. 
        
        text = f'Todays Morining Update - {datetime.date.today().strftime("%d %b %Y")}'

        #Format weather
        if self.content['weather']['include'] and self.content['weather']['content']:
            text += f"Todays Weather for {self.content['weather']['content']['city']}, {self.content['weather']['content']['country']}\n\n"
            for daily_forcast in self.content['weather']['content']['periods']:
                text += f'{daily_forcast["timestamp"].strftime("%d %b %H%M")} - {daily_forcast["temp"]}\u00B0C | {daily_forcast["description"]}\n'
            text += '/n'

        #Format scores
        if self.content['scores']['include'] and self.content['scores']['content']:
            text += ' Yesterdays NBA Scores\n\n'
            for scores in self.content['scores']['content']:
                text += f'{scores["Home Team"]} | {scores["Home Score"]} \n {scores["Away Team"]} | {scores["Away Score"]}'############
            text += '\n'

        #Format headlines
        if self.content['headlines']['include'] and self.content['headlines']['content']:
            text += ' Todays Headlines\n\n'
            for headline in self.content['headlines']['content']:
                text += f'{headline["Source"]}\n {headline["Headline"]}\n {headline["Description"]}\n {headline["Link"]} '###########
            text += '\n'

        #Format word
        #if self.content['word']['include'] and self.content['word']['content']:
            #text += ' Todays Word\n\n'
            #text += f'"{self.content['word']['content']}"'

        #Generate html for email

        html = f"""<html>
    <body>
    <center>
        <h1>Daily Digest - {datetime.date.today().strftime('%d %b %Y')}</h1>
        """

        # format weather quote
        if self.content['weather']['include'] and self.content['weather']['content']:
            html += f"""
        <h2>Forecast for {self.content['weather']['content']['city']}, {self.content['weather']['content']['country']}</h2>
        <table>
                    """

            for forecast in self.content['weather']['content']['periods']:
                html += f"""
            <tr>
                <td>
                    {forecast['timestamp'].strftime('%d %b %H%M')}
                </td>
                <td>
                    <img src="{forecast['icon']}">
                </td>
                <td>
                    {forecast['temp']}\u00B0C | {forecast['description']}
                </td>
            </tr>
                        """               

            html += """
            </table>
                    """

        # format scores
        if self.content['scores']['include'] and self.content['scores']['content']:
            html += f"""
        <h2>Yesterdays NBA Scores</h2> 
        <table>
                    """

            for scores in self.content['scores']['content']: ####################
                html += f"""
            <tr>
                <td>
                    {scores['Home Team']} | {scores['Home Score']}
                </td>
                <td>
                    {scores['Away Team']} | {scores['Away Score']}
                </td>
            </tr>
                        """               

            html += """
            </table>
                    """

        # format headlines
        if self.content['headlines']['include'] and self.content['headlines']['content']:
            html += f"""
        <h2>Todays Headlines</h2> 
        <table>
                    """

            for headlines in self.content['headlines']['content']: ###########
                html += f"""
            <tr>
                <td>
                    {headlines['Source']}
                </td>
                <td>
                    {headlines['Headline']}
                </td>
                <td>
                    {headlines['Description']}
                </td>
                <td>
                    {headlines['Link']}
                </td>
            </tr>
                        """               

            html += """
            </table>
                    """
        # format daily word
        #if self.content['word']['include'] and self.content['word']['content']:
            #html += f"""
        #<h2>Word of the Day</h2>
        #<p>"{self.content['word']['content'][0]['word']} : {self.content['word']['content']['definitions'][0]['definition']} "</p>
             #       """

        # footer
        html += """
    </center>
    </body>
</html>
                """ 
        return {'text' : text, 'html' : html}

if __name__ == '__main__':
    email = DailyEmail()

email.send_email()