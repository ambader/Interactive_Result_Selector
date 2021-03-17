import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt

def mk_option_list(inp):
    zw_list={}
    for i in inp.get_partitions()[0].keys():
        zw=[]
        for j in inp.get_partitions():
            zw.append(j[i])
        zw_list.update({ i : set(zw)})
    return zw_list

def mk_dropdown_menue(inp):
    zw=mk_option_list(inp)
    for i in zw.keys():
        exec(str(i)+"=widgets.Dropdown(options="+str(zw[i])+", description='"+str(i)+"')", globals())
        exec("display("+str(i)+")", globals())
        
def recent_choice(inp):
    ll=mk_option_list(inp).keys()
    out=[]
    for i in ll:
        zw=eval(i+".value")
        out.append(zw)
    return out

def display_IRS(inp):
    %matplotlib inline
    %config InlineBackend.close_figures=True
    
    mk_dropdown_menue(inp)
    
    output = widgets.Output()
    button = widgets.Button(description="Show Plot")
    
    display(button,output)
    
    def on_button_clicked(b):
        with output:
            for i in inp.get_partitions():
                if [*i.values()]==recent_choice(inp):
                    inp.get_result_for_partition(i).df_plot.plot()
                else:
                    pass
        clear_output()
        mk_dropdown_menue(inp)
        display(button,output)
            
    button.on_click(on_button_clicked)
