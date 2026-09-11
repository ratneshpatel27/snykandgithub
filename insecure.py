import pickle
# VULNERABLE
def load_data(serialized_data):
    return pickle.loads(serialized_data)
