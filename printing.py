from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os

THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR=os.path.dirname(THIS_FILE_PATH)
REPORT_path =  os.path.join(BASE_DIR,"reports")
#['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

def print_report(fname,arr,res):
    res=round(res[0][0][0]*100,2)
    env = Environment(loader=FileSystemLoader('.'))
    TEMPLATE_FILE=os.path.join(BASE_DIR,'template.html')
    if os.path.exists(TEMPLATE_FILE): 
        template = env.get_template("template.html")
        template_vars = {"name" : fname,
                        "age": arr[7],
                        "preg":arr[0],
                        "glucose":arr[1],
                        "bp":arr[2],
                        "sk_thick":arr[3],
                        "insu":arr[4],
                        "bmi":arr[5],
                        "dpi":arr[6],
                        "result":res
                    }

        html_out = template.render(template_vars)
        os.makedirs(REPORT_path,exist_ok=True)
        fname="reports/"+fname.replace(" ","_")+"_report.pdf"
        HTML(string=html_out).write_pdf(fname)
        return True
    else:
        return False