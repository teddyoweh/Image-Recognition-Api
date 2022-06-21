
from flask import render_template, Blueprint, request
from app.models import iMatchApi
from flask import jsonify
from app import main
#blueprint = Blueprint('views', __name__)


################
#### routes ####
################


@main.route('/imatch',methods=['GET'])
def imatch():
    img1 = request.args.get('img1')
    img2 = request.args.get('img2')
    ############# Debugging output ############
    print('[%] Comparing {} against {}'.format(img1,img2))
    ###########################################
    
    
    output = {'img1':img1,'img2':img2,'result':iMatchApi(img1,img1).imatch()}
    response = {request.remote_addr:output}
    
    
    ############# Debugging output ############
    print(response)
    ###########################################
    
    
    return jsonify(output)


 