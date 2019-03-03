# Healthelf- your personal health monitor
- This is a project for SteelHeck2019
- This project focus on monitoring heartbeat and reporting irregular heart rate. Add features to google home and Fitbit.



## Team member
- Ruochi Zhang ([GitHub](https://github.com/zhangruochi))
- Tianqi Xie ([Github](https://github.com/kikixie95))
- Xiaoqian Xu ([GitHub](https://github.com/Cecilia-xu))
- Zhehao Guo ([GitHub](https://github.com/PaulGuo5))
- Qi Lu ([GitHub](https://github.com/FawneLu))


## Inspiration
- Health rate is an important index for assessing people's health condition. We implemented an application to monitor people's heartbeat rate all day.
- We found that Google home cannot support health care, and Fitbit cannot support data analysis. To tackle the drawbacks, we extended two features for each device.

## What it does
The user who wears Fitbit will be monitored by our application and generate and analyze full dataset at the back-end. The user can get a health report every day by speaking to google home and the user can also send the report to the doctor or others through google home. Once an irregular heartbeat rate was found, the user will get the result in the report. Moreover, the user can check out the full report on the website(www.healthelf.net).

## How we built it
- connect and modify hardwares (Google home, Fitbit)
- Use Fitbit API to get user's dataset
- Use machine-learning algorithms to train a neural network model to predict the heartbeat rate ( This step performed on the google cloud platform)
- Find the outliner by evaluating the Pearson coefficient.
- Register a domain name ( On domain.com)
- Use GitHub-pages and hexo to built a website which can visualize the heartrate report.
- Train the google home to get respond in real-time and get a detailed report by sending email

## Challenges we ran into
- It is not very easy to access the Google Home Mini to the mobile App.
- We finally use Google API to send the request to the Google Home Mini, which sends us responses. The approach is realize is far more challenge for us.
- We would like to run the code on Google Platform but we find difficulties to apply the APIs.
- It is very hard for us to launch the software we need on the Raspberry but we did not find a fair good way to solve. Thus, we abandon it.
- We want to push our result on the GitHub. At first, we wanted to use the platform provided by domain.com, but our data can’t connect to the website. So we used GitHub pages and hero to realize it.
- We wanted to let the electronic arm perform as the home appliance but it doesn’t have specialist USB tools to connect to the raspberry or our laptop. So we abandon it.

## Accomplishments that we're proud of
Compensate the drawbacks of two devices and help people keep healthy.

## What we learned
It is a really good chance for us to use various kinds of APIs of different tools. We overcame many troubles when we met with different problems, just as we discussed the challenges above. And we learn more about the significance of teamwork.

## What's next for Healthelf- your personal health monitor
- We need to improve the report by monitoring more health index
- We need to improve the user experience

## Try it out
-  [healthelf](www.healthelf.com)