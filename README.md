## Deployment

[admin](http://ec2-18-196-157-226.eu-central-1.compute.amazonaws.com/admin/)
[blog](http://ec2-18-196-157-226.eu-central-1.compute.amazonaws.com/blog/)

## Useful commands

### Tests

tests
> python manage.py test 

Tests to create coverage
> coverage run --source='.' manage.py test 
> coverage report
> coverage html

### Docker
Spin up containers
> docker-compose up -d --build

Run tests
> docker-compose exec django python manage.py test

Check logs on django service
> docker-compose logs -f django	


**Improvements**
Increase coverage of tests
Configure SSL