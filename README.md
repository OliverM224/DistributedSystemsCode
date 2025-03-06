# DistributedSystemsCode
Repository with material and code for the "Distributed and Cloud Computing" module, 
You can view the twitter bot here! https://x.com/dev31770 

This repo uses AWS' Lambda Function service to recieve data from IOT sensors, and publish flood alerts onto a twitter account.

Installation Guide:
1. Sign up for the Twitter Developers Program through the online Developer Portal: 
   <ul>
     <li>After signing up, generate an API Key, Secret API Key, Access Token, and Secret Access Token</li>
     <li>Make sure to fill out the user authentication form in order to grant your project read write access! If the form asks you for a URL for 0auth, it's recomended to just provide a link to your own twitter page.</li>
   </ul>

2. Create the lambda function:
   Log into your AWS account and create your own lambda function.
   <ul>
     <li>When configuring your lambda function, choose the Python 3.9 runtime and x86 architecture.</li>
      <li>Copy and paste the contents of twitter.py into the lambda function, make sure to add your API keys into the highlighted tweepy client area.</li>
   </ul>
   
   Speaking of tweepy...

3. Import Tweepy
   Tweepy is a python library used to make easy api calls to twitter. In order to import it to your lambda function, take the tweepy files from this repo, and package them into a zip file with the following structure

   folderName/python/tweepyfolders
   
   its important that the tweepy library is stored inside a directory called python, otherwise AWS won't recognise it.

   You can then import it into AWS using the lambda functions layer system. Just click on the layers option at the bottom of your lambda function's page, and drag and drop the zip.

5. Test it!
   Open the test JSON file and add your test data to the event json window! An example is listed below:
   {
     "dateTime": "05/03/2025",
     "Location": "River Orwell",
     "Severity": "High"
   }
   then hit run and check your twitter page. Congrats!
