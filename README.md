# About

This project helps you build and deploy an API server with just a few settings. 



# Just Do it

1. I assume you are subscribed to AWS and have user rights associated with beanstalk. It also assumes you have a remote database server such as RDS. Under this assumption, the README was written.

   ​

2. git clone https://github.com/limdongjin/boilerplate_drf_elasticbeanstalk

   ​

3. Install python 3.6 or using virtual environment

   ​

4. pip install -r requirements.txt ( if you have both pip and pip3 , you must use pip3 )

    

5. Set your database information to iotd/iotd/config.py file
  
  5-2. If you do not want to commit the information in config.py to git, you can store the information in the environment variables of the AWS Elastic Beanstalk distribution server. If you want to save it in an environment variable, you should remove the config.py file.

  ​

6. Set Django's secret_key to iotd/iotd/config.py file

   ​

7. Write your Model to iotd/index/models.py 

   7-2. if you want to use existing table from an existing database,  
   ​          "python iotd/manage.py inspectdb > iotd/index/models.py"
   7-3. if you want to use new table, 
   ​          "python iotd/manage.py makemigrations & python iotd/manage.py migrate"

8. Write your Model's Serializer to iotd/index/serializers.py 

   8-2. An example is written as a comment in the file.

9. "python iotd/manage.py createsuperuser"

10.  git add . & git commit -m "deploy"
   9-2.  If you are using a public repository, be careful not to push the config file. Be sure to register the config information as an environment variable on the distribution server. How to register an environment variable can be confirmed by entering the AWS elastic beanstalk dashboard

   ​

11. eb init 

   ​

12. eb create

    ​

13. you will see Success 

    ​

14.  if you update deployment server, 

    "eb deploy" 

# Dependency

1. python 3.6
2. DRF and Django
3. Django Rest Swagger
4. White noise
5. AWS Elastic Beanstalk
6. Mysql
7. Linux or Mac
