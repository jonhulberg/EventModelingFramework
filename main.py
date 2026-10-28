import json
import os
import shutil
import numpy as np
import pandas as pd
import modeling_routines.modeling_routine as algorithm

class EventModelingFramework:
    def __init__(self,cb2rges_json_path: str, pyAethra_json_path: str, jacsanomaly_json_path: str, modeling_instructions_json_path: str):

        # The structure of the pyAethra and jacsanomaly jsons are undecided.
        # But we definitely must read them in!


        with open(cb2rges_json_path) as f:
            self.cb2rges_json = json.load(fp=f)

        # Just a placeholder. Depends on what Jay outputs. Also this may all be accumulated in the jacsanomaly JSON. Lots to be defined
        self.RA = self.cb2rges_json['RA']
        self.dec = self.cb2rges_json['dec']
        self.event_ID = self.cb2rges_json['event_ID']


        with open(pyAethra_json_path) as f:
            self.pyAethra_json = json.load(fp=f)

        with open(jacsanomaly_json_path) as f:
            self.jacsanomaly_json = json.load(fp=f)

        #The specifics of what we do with these depends on what's in them.


        # This is more for the ICGS. It reads the grid settings in as a JSON.

        if modeling_instructions_json_path is not None:
            with open(self.jacsanomaly_json['modeling_instructions_path']) as f:
                self.modeling_instructions_json = json.load(fp=f)
        # this allows us to tell the code what algorithm is being used.
        # then it won't trigger on events that should use a different algorithm.
        # Valerio and I thought a container for each different modeling algorithm would be best.
        # So this is a way to tell each RTModel to skip RTModel + ICGS events and vice-versa.
        # We could also hardcode it in the version that goes in each container.
        # Perhaps we write separate functions for each modeling routine and put them in a small package
        # perhaps we just maintain a separate version of this framework for each modeling routine.
        # Then have the function self.modeling_routine() call the different function

        self.modeling_algorithm = self.jacsanomaly_json['suggested_algorithm'] #could hardcode
        self.satellite_dir = "/placeholder"  # hardcoded most likely.
        self.limb_darkening_file = self.modeling_instructions_json['limb_darkening_file'] # maybe it's None
        self.RTModel_events_directory = self.modeling_instructions_json['RTModel_events_directory']


    def construct_rtmodel_directory(self):
        """
        depends on format of data from cb2rges, pyAethra, jacsanomaly.
        :return: None
        """
        print("Under Construction!")


    def modeling_routine(self):
        """
        RTModel routine called here.
        """
        algorithm.main()
        print("Under Construction!")

    def create_modeling_output(self  ):
        output_dict = {}
        output_dict["RTModel_event_directory"] = RTModel_event_directory
        return output_dict

    def run(self):
        self.construct_rtmodel_directory()
        self.modeling_routine()
        self.create_modeling_output()
