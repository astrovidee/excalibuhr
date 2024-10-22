from excalibuhr import pipeline

workpath = './Users/astrovidee/Dropbox/hip65426_project/excalibuhr'
night = '2024-02-27'

ppl = pipeline.CriresPipeline(
                              workpath, night=night, obs_mode='nod',
                              num_processes=4, clean_start=False
                             )

username = 'vidyav1' #your ESO username
program_id = '110.23RW'

ppl.download_rawdata_eso(login=username, prog_id=program_id)