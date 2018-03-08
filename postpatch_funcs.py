
import pandas as pd

def nucleated(x):
    nucleus = x[(x["Post patch?"] == "Nucleated") | (((x["Post patch?"] == "nucleus_visible") | (x["Post patch?"] == "nucleus_present")) & (x["Post patch pipette R"] >= 500))]
    return nucleus

def partial_nucleated(y):
    partial = y[(y["Post patch?"] == 'Partial-Nucleus') | (((y['Post patch?'] == 'nucleus_present') | (y['Post patch?'] == 'nucleus_visible')) & (y["Post patch pipette R"] <= 499))]
    return partial

def outside_out(z):
    outside = z[(z["Post patch?"] == 'Outside-Out') | (((z['Post patch?'] == 'nucleus_absent') | (z['Post patch?'] == 'no_nucleus_visible')) & (z['Post patch pipette R'] >= 500))]
    return outside

def no_seal(w): 
    no = w[(w["Post patch?"] == 'No-Seal') | (((w['Post patch?'] == 'nucleus_absent') | (w['Post patch?'] == 'no_nucleus_visible')) & (w['Post patch pipette R'] <= 499))]
    return no
    
def entire_cell(v):
    entire = v[(v["Post patch?"] == 'Entire-Cell') | (v['Post patch?'] == 'entire_cell')]
    return entire


def reclassify(df):
    oo = outside_out(df)
    oo['post patch class'] = 'Outside out'
    nu = nucleated(df)
    nu['post patch class'] = 'Nucleated'
    ns = no_seal(df)
    ns['post patch class'] = 'No seal'
    pn = partial_nucleated(df)
    pn['post patch class'] = 'Partial nucleated'
    ec = entire_cell(df)
    ec['post patch class'] = 'Entire cell'
    return  nu, pn, oo, ns, ec

#out, nuc, noseal, partnuc, ent = reclassify(ps)

def concat_df(a, b, c, d, e):
    frames = (a, b, c, d, e)
    df = pd.concat(frames)
    return df

def postpatch_reclass(df):
	return concat_df(*reclassify(df))


#concat_df(*reclassify(ps))
    
#ps = concat_df(out, nuc, noseal, partnuc, ent)    

#ps