import logging.handlers

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Handler 
LOG_FILE = '/tmp/sample-app.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add Formatter to Handler
handler.setFormatter(formatter)

# add Handler to Logger
logger.addHandler(handler)

welcome = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>Mark Retail Warehouse Management System</title>
  <link href="./css/tabs.css" rel="stylesheet" />
  <!--<link href="./css/main.css" rel="stylesheet" />-->
  <!--<link href="./css/font-awesome.min.css" rel="stylesheet" />-->
<!-- Compiled and minified CSS -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

<!-- Compiled and minified JavaScript -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>

  <script src="./js/jquery-1.11.0.min.js"></script>
  <script src="./js/bootstrap.min.js"></script>
  <script src="https://sdk.amazonaws.com/js/aws-sdk-2.481.0.min.js"></script>
  <script src="./js/product.js"></script>
  <script src="./js/demand.js"></script>
  <script src="./js/administrator.js"></script>
  <script src="./js/tabs.js"></script>
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col-sm-6">
        <h2 style="background-color:rgb(64, 139, 224);color:white;">Mark Retail Warehouse Administration</h2>
      </div>
    </div>
    <div class="tab" style="background-color:rgb(64, 139, 224);color:white;">
      <button class="tablinks" onclick="opencomp(event, 'Products')">Products</button>
      <button class="tablinks" onclick="opencomp(event, 'Demands')">Demands</button>
      <button class="tablinks" onclick="opencomp(event, 'Administrators')">Administrators</button>
    </div>
    <div id="Products" class="tabcontent active">
        <div class="row">
            <div class="col-sm-6">
              <div class="panel panel-primary">
                <div class="panel-heading">
                  Product
                </div>
                <div class="panel-body">
                  <div class="form-group">
                    <label for="Productid">
                      Product id
                    </label>
                    <input type="text"
                          class="form-control"
                          id="Productid" />
                  </div>
                
                    <div class="form-group">
                      <label for="Productname">
                        Product Name
                      </label>
                      <input type="text"
                            class="form-control"
                            id="Productname" />
                    </div>
                    
                      <div class="form-group">
                        <label for="ProductSKU">
                          Product SKU
                        </label>
                        <input type="text"
                              class="form-control"
                              id="ProductSKU" />
                      </div>
                  
                        <div class="form-group">
                          <label for="Productweight">
                            Product Weight
                          </label>
                          <input type="text"
                                class="form-control"
                                id="Productweight" />
                        </div>
    
                </div>
                <div class="panel-footer">
                  <div class="row">
                    <div class="col-xs-12">
                      <button type="button" id="updateButton" style="background-color:rgb(64, 139, 224);"
                              class="btn btn-primary"
                              onclick="addProduct();">
                        Add
                      </button>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-sm-6">
                    <table id="ProductTable"
                          class="table table-bordered table-condensed table-striped">
                      <thead>
                        <tr>
                          <th>id</th>
                          <th>Name</th>
                          <th>SKUs</th>
                          <th>Weight</th>
                        </tr>
                      </thead>
                    </table>
                  </div>
                </div>
          </div>
        </div>
      </div>
    </div>
    <div id="Demands" class="tabcontent active">
        <div class="row">
            <div class="col-sm-6">
              <div class="panel panel-primary">
                <div class="panel-heading">
                  Demand
                </div>
                <div class="panel-body">
                  <div class="form-group">
                    <label for="Demandid">
                      Demand id
                    </label>
                    <input type="text"
                          class="form-control"
                          id="Demandid" />
                  </div>
                
                    <div class="form-group">
                      <label for="Demandquantity">
                        Demand Quantity
                      </label>
                      <input type="text"
                            class="form-control"
                            id="Demandquantity" />
                    </div>
                    
                      <div class="form-group">
                        <label for="Demandstore">
                          Store name
                        </label>
                        <input type="text"
                              class="form-control"
                              id="Demandstore" />
                      </div>
                  
                        
    
                </div>
                <div class="panel-footer">
                  <div class="row">
                    <div class="col-xs-12">
                      <button type="button" id="updateButton" style="background-color:rgb(64, 139, 224);"
                              class="btn btn-primary"
                              onclick="addDemand();">
                        Add
                      </button>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-sm-6">
                    <table id="DemandTable"
                          class="table table-bordered table-condensed table-striped">
                      <thead>
                        <tr>
                          <th>id</th>
                          <th>Quantity</th>
                          <th>Store Name</th>
                        </tr>
                      </thead>
                    </table>
                  </div>
                </div>
          </div>
        </div>
      </div>
    </div>
    <div id="Administrators" class="tabcontent active">
        <div class="row">
            <div class="col-sm-6">
              <div class="panel panel-primary">
                <div class="panel-heading">
                  Administrator
                </div>
                <div class="panel-body">
                  <div class="form-group">
                    <label for="Administratorid">
                      Administrator id
                    </label>
                    <input type="text"
                          class="form-control"
                          id="Administratorid" />
                  </div>
                
                    <div class="form-group">
                      <label for="Administratorname">
                        Administrator Name
                      </label>
                      <input type="text"
                            class="form-control"
                            id="Administratorname" />
                    </div>
                    
                  
                        <div class="form-group">
                          <label for="Administratoremail">
                            Administrator Email
                          </label>
                          <input type="text"
                                class="form-control"
                                id="Administratoremail" />
                        </div>
    
                </div>
                <div class="panel-footer">
                  <div class="row">
                    <div class="col-xs-12">
                      <button type="button" id="updateButton"  style="background-color:rgb(64, 139, 224);"
                              class="btn btn-primary"
                              onclick="addAdministrator();">
                        Add
                      </button>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-sm-6">
                    <table id="AdministratorTable"
                          class="table table-bordered table-condensed table-striped">
                      <thead>
                        <tr>
                          <th>id</th>
                          <th>Name</th>
                          <th>Email Address</th>
                        </tr>
                      </thead>
                    </table>
                  </div>
                </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</body>
</html>

"""


def application(environ, start_response):
    path = environ['PATH_INFO']
    method = environ['REQUEST_METHOD']
    if method == 'POST':
        try:
            if path == '/':
                request_body_size = int(environ['CONTENT_LENGTH'])
                request_body = environ['wsgi.input'].read(request_body_size)
                logger.info("Received message: %s" % request_body)
            elif path == '/scheduled':
                logger.info("Received task %s scheduled at %s", environ['HTTP_X_AWS_SQSD_TASKNAME'],
                            environ['HTTP_X_AWS_SQSD_SCHEDULED_AT'])
        except (TypeError, ValueError):
            logger.warning('Error retrieving request body for async work.')
        response = ''
    else:
        response = welcome
    start_response("200 OK", [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(response)))
    ])
    return [bytes(response, 'utf-8')]
