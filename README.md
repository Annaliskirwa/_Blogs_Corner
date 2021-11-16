# Blogs Corner  
#### 16/11/2021  
#### By **Annalis Kirwa**  
## Description  
This is a personal blogging web application where people share ideas and opinions and others can read them.
There is also a feature for random quotes display just to inspire the readers
## Behaviour Driven Development(BDD) 

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Writer/Blogger Authentication | **On demand** | Access Admin dashboard |
| Display blogs by most recent | **Home page** | Clickable links to open all blogs |
| Display profile | **Click profile page** | Redirected to a page with your profile |
| Display single blogs | **On link click** | Blog is displayed with comment ready function plus any comments already stored |
| To add a blog  | **Through Admin dashboard** | Redirected to the new blog form collection form|
| To edit a blog  | **Through Admin dashboard** | Redirected to the  blog form collection form and editing happens|
| To delete a blog/comments  | **Through Admin dashboard and on displays** | Bad comments and posts can be deleted|
| To subscribe  | **On button click** | Users can subscribe on click|

 ## Features 
 As a user of Pitch Hub web application, you will be able to: 
 * view the blog posts on the site   
 * comment on blog posts    
 * view the most recent posts    
 * email alert when a new post is made by joining a subscription    
 * see random quotes on the site    
 * sign in to the blog.    
 * create a blog from the application   
 * delete comments that I find insulting or degrading  
 * update or delete blogs I have created.  
 
 ## Setup/Installation Requirements  
 ### To interact with the Blogs corner web application:   
* Have the latest version of browser installed  
* Click on this <a href = "https://blogs-corner.herokuapp.com/">link</a> to view blogs and see random quotes. 
  
 ### To contribute to the web application project:  
Make sure you have the following installed:  
```
Pip
Python version 3.6
Flask
virtualenv
postgres
```  
* Create an account on Github
* Fork the repository from Github with this <a href = "https://github.com/Annaliskirwa/_Blogs_Corner" >link </a>
* Clone the repository
* Open the project cloned project   
* Install virtual environment using `$ python3.6 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `python3.6 pip install -r requirements.txt`
* Create a `start.sh` file in the root of the folder   

* Edit the configuration instance in `manage.py` by commenting on `production` instance and uncommenting `development` instance
* To run the application, in your terminal:

        $ chmod a+x start.sh
        $ ./start.sh  
   
   
## Known Bugs
There are no known bugs so far
## Technologies Used  
* Python v3.6  
* HTML
* Bootstrap
* Flask  
* Postgres  
* Quotes API
## Support and contact details
In case of any problem while interacting with the web application, reach out to me at annalis.kirwa@student.moringaschool.com
### License.
MIT Copyright (c) 2021 **[MITlicense](LICENSE)**
