from flask_restful import Resource, Api, request
from waterSys import app, moisture_sensor, valve_controller
import json
from datetime import datetime

api = Api(app)

class Moisture_Percent(Resource):
    def get(self):
        currDT = datetime.now()
        hour = currDT.hour

        moisture_output = {
            'timeStamp': currDT,
            'hour': hour, 
            'moisturePercent': moisture_sensor.moisture_readout()      
        }

        return json.dumps(moisture_output, default=str)

class Valve_Status(Resource):
    def get(self):
        currDT = datetime.now()

        status = {
         'timeStamp': currDT,
         'valveStatus': valve_controller.valve_status()
        }

        return json.dumps(status, default=str)

class Valve_Controller(Resource):
    def post(self):
        data = request.get_json(force=True)

        valve_controller.valve_controller(data['valve'])

        return json.dumps({'valveStatus': valve_controller.valve_status()})

api.add_resource(Moisture_Percent, '/moisture_percent')
api.add_resource(Valve_Status, '/valve_status')
api.add_resource(Valve_Controller, '/valve_controller')