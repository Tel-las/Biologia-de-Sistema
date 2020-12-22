from cobra.io import load_json_model
import cobra
model = cobra.io.load_json_model('iEK1011_inVivo_media.json')
print(model.summary())
model_bounds = {r.id:(r.lower_bound, r.upper_bound) for r in model.reactions}
for i in model_bounds:
    print(i, model_bounds[i])