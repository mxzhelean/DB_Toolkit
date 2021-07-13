def cache_to_file(f):
    """
    This should be used to decorate methods that return dataframes.
    The decorator will store the results of method call to a file.
    subsequent calls to the method will pull the data from the
    file if the file exists.
    
    Decorated functions should include a filename and force parameter.
    If these are not included, the decorator will quietly do nothing.
    
    the force parameter can be used to force a refresh of the data.
    this will rebuild the dataframe and store the new results in the
    file.
    
    The target use is to decorate methods that query for data.
    
    If loading the file fails for any reason, forced behavior will be used.
    """
    import os
    import pandas as pd
    def new_f(*args, **kwargs):
        filename = kwargs.get('filename', None)
        force = kwargs.get('force', False)
                
        if not force and filename and os.path.isfile(filename):
            try:
                return pd.read_csv(filename)
            except Exception as e:
                pass
        df = f(*args, **kwargs)
        if filename:
            df.to_csv(filename, index=False)
        return df
    return new_f
