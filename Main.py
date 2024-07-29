#THIS IS THE MAIN FILE. START THE CODE FROM HERE
#TODO: Need to get reddit API and gather data


from Reddit.RedditMain import Reddit_start
from Email.EmailMain import send_email
from GPT.GPTMain import GPT_start

def initialize_email_service(Recipiants, Body):
    print("Initializing Email...")
    for email_address in Recipiants:
        send_email(email_address, Body)
        print("Email sent to " + email_address)



def start():
    print("Program Startup")
    subreddit_list = Reddit_start()
    print("Subreddits accessed") 
    # initialize_email_service(['6jellydonuts@gmail.com'], "Tesing body")
    message = GPT_start(subreddit_list)
    print(message)
    initialize_email_service(['6jellydonuts@gmail.com', 'artley0606@gmail.com'], message)




if __name__ == '__main__':
    start()
    # email_test()