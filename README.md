# DistributedSystemsCode
Repository with material and code for the "Distributed and Cloud Computing" module, 
You can view the twitter bot here! https://x.com/dev31770 

This repo uses AWS' Lambda Function service to recieve data from IOT sensors, and publish flood alerts onto a twitter account.

Installation Guide:
1. Sign up for the Twitter Developers Program through the online Developer Portal: 
   <ul>
     <li>After signing up, generate an API Key, Secret API Key, Access Token, and Secret Access Token</li>
     <li>Make sure to fill out the user authentication form in order to grant your project read write access!</li>
   </ul>

2. Create the lambda function:
   Log into your AWS account and create your own lambda function.
   <ul>
     When configuring your lambda function, choose the Python 3.9 runtime and x86 architecture.
   </ul>
   Copy and paste the 
