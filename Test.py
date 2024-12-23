from excalibuhr import pipeline

workpath = './'
night = '2023-06-06'

ppl = pipeline.CriresPipeline(
                              workpath, night=night, obs_mode='nod',
                              num_processes=4, clean_start=False
                             )

#ppl.extract_header()
#ppl.cal_dark()
#ppl.cal_flat_raw()
#ppl.cal_flat_trace()
ppl.cal_slit_curve()