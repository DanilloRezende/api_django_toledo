import json
from datetime import datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from backend.core.models import Bulk_Batchs, Bulk_Weigths, Lote, events


@require_http_methods(['GET'])
def lote_list(request):
    lotes = Lote.objects.all()
    data = [lote.to_dict() for lote in lotes]
    return JsonResponse({'data':data})

@require_http_methods(['GET'])
def lote_detail(request, pk):
    lote = Lote.objects.get(pk=pk)
    data = lote.to_dict()
    return JsonResponse({'data':data})

# View para receber um lote a partir da tabela PRIXHISTTOLBAG
@csrf_exempt
@require_http_methods(['POST'])
def lote_create(request):
    if request.body:
        data = json.loads(request.body)
        print(data) 
        try:
            get_id = data["id"]
        except:
            get_id = None
        print(data) 
        try:
            get_lote = data["batch"]
        except:
            get_lote = None
        try:
            get_production_date = data["production_date"]
        except:
            get_production_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        formatted_date = datetime.strptime(get_production_date, "%Y-%m-%d %H:%M")     
     
        try:
            get_terminal = data["terminal"]
        except:
            get_terminal = None
        try:
            get_sequencial = data["sequencial"]
        except:
            get_sequencial = None
        try:
            get_type = str(data["type"]).rstrip()
        except:
            get_type = None
        try:
            get_liquid = float(data["liquid"])
        except:
            get_liquid = None
        try:
            get_tara = float(data["tara"])
        except:
            get_tara = None
        try:
            get_unit_of_measurement = str(data["unit_of_measurement"]).rstrip()
        except:
            get_unit_of_measurement = None
        try:
            get_client = str(data["client"]).rstrip()
        except:
            get_client = None
        try:
            get_product_number = int(data["product_number"])
        except:
            get_product_number = None
        try:
            get_product_name = str(data["product_name"]).rstrip()
        except:
            get_product_name = None
        try:
            get_sub_total = float(data["sub_total"])
        except:
            get_sub_total = None
        try:
            get_total = float(data["total"])
        except:
            get_total = None
        try:
            get_message = str(data["message"]).rstrip()
        except:
            get_message = None


        Lote.objects.create(
            id = get_id,
            batch = get_lote,
            production_date = formatted_date,
            terminal = get_terminal,
            sequencial = get_sequencial,
            type = get_type,
            liquid = get_liquid,
            tara = get_tara,
            unit_of_measurement = get_unit_of_measurement,
            client = get_client,
            product_number = get_product_number,
            product_name = get_product_name,
            sub_total = get_sub_total,
            total = get_total,
            message = get_message,
        )
        return JsonResponse({"message": "Lote not found on Database!"})


# View para receber um evento a partir da tabela TB_BULK_EVENTS
@csrf_exempt
@require_http_methods(['POST'])
def bulk_events(request):
    if request.body:
        data = json.loads(request.body)
        try:
            get_eventID = data["eventID"]
        except:
            get_eventID = None
        try:
            get_terminal = data["terminal"]
        except:
            get_terminal = None
        try:
            get_dateTime = data["dateTime"]
        except:
            get_dateTime = datetime.now().strftime("%Y-%m-%d %H:%M")
        formatted_date = datetime.strptime(get_dateTime, "%Y-%m-%d %H:%M")
        try:
            get_evtType = data["evtType"]
        except:
            get_evtType = None
        try:
            get_evtCode = data["evtCode"]
        except:
            get_evtCode = None
        try:
            get_evtMessage = str(data["evtMessage"]).rstrip()
        except:
            get_evtMessage = None
        
        events.objects.create(
            eventID = get_eventID,
            terminal = get_terminal,
            dateTime = formatted_date,
            evtType = get_evtType,
            evtCode = get_evtCode,
            evtMessage = get_evtMessage,
            
        )
        return JsonResponse({"message": "Lote not found on Database!"})


# View para receber um lote a partir da tabela TB_BULK_STD_BATCHES
@csrf_exempt
@require_http_methods(['POST'])
def bulk_STD_batches(request):
    if request.body:
        data = json.loads(request.body)
        get_batchID = data["batchID"]
        try:
            get_terminal = data["terminal"]
        except:
            get_terminal = None
        try:
            get_batchStatus = data["batchStatus"]
        except:
            get_batchStatus = None
        try:
            get_terminal = data["terminal"]
        except:
            get_terminal = None
        try:
            get_userField1 = data["userField1"]
        except:
            get_userField1 = None  
        try:
            get_userField2 = data["userField2"]
        except:
            get_userField2 = None
        try:
            get_userField3 = data["userField3"]
        except:
            get_userField3 = None
        try:
            get_userField4 = data["userField4"]
        except:
            get_userField4 = None
        try:
            get_userField5 = data["userField5"]
        except:
            get_userField5 = None    
        try:
            get_userField6 = data["userField6"]
        except:
            get_userField6 = None  
        try:
            get_prodNumberList = str(data["prodNumberList"]).rstrip()
        except: 
            get_prodNumberList = None
        try:
            get_subtotNumberList = str(data["subtotNumberList"]).rstrip()
        except: 
            get_subtotNumberList = None
        try:
            get_targetValueList = str(data["targetValueList"]).rstrip()
        except:
            get_targetValueList = None
        
       


        Bulk_Batchs.objects.create(
            batchID = get_batchID,
            terminal = get_terminal,
            batchStatus = get_batchStatus,
            userField1 = get_userField1,
            userField2 = get_userField2,
            userField3 = get_userField3,
            userField4 = get_userField4,
            userField5 = get_userField5,
            userField6 = get_userField6,
            prodNumberList = get_prodNumberList,
            subtotNumberList = get_subtotNumberList,
            targetValueList = get_targetValueList,

        )
        return JsonResponse({"message": "Lote not found on Database!"})

# View para receber um lote a partir da tabela TB_BULK_WEIGHTS
@csrf_exempt
@require_http_methods(['POST'])
def bulk_weigths(request):
    if request.body:
        data = json.loads(request.body)
        try:
            get_weightID = data["weightID"]
        except: 
            get_weightID = None
        try:
            get_dateTime = data["dateTime"]
        except:
            get_dateTime = datetime.now().strftime("%Y-%m-%d %H:%M")
        formatted_date = datetime.strptime(get_dateTime, "%Y-%m-%d %H:%M")
        try:        
            get_opType = str(data["opType"]).rstrip()
        except:
            get_opType = None
        try:
            get_terminal = data["terminal"]
        except:
            get_terminal = None
        try:
            get_net = float(data["net"])
        except:
            get_net = None
        try:
            get_tare = float(data["tare"])
        except:
            get_tare = None
        try:
            get_wtUnit = str(data["wtUnit"]).rstrip()
        except:
            get_wtUnit = None
        try:
            get_stepNumber = data["stepNumber"]
        except: 
            get_stepNumber = None
        try:
            get_subtotNumber = data["subtotNumber"]
        except:
            get_subtotNumber = None
        try:     
            get_prodNumber = data["prodNumber"]
        except: 
            get_prodNumber = None        
        try:
            get_stepTotal = float(data["stepTotal"])
        except:
            get_stepTotal = None
        try:
            get_subtotTotal = str(data["subtotTotal"]).rstrip()
        except:
            get_subtotTotal = None
        try:
            get_prodTotal = float(data["prodTotal"])
        except:
            get_prodTotal = None
        try:
            get_grandTotal = float(data["grandTotal"])
        except:
            get_grandTotal = None
        try:
            get_flow = float(data["flow"])
        except:
            get_flow = None
        try:
            get_flowUnit = str(data["flowUnit"]).rstrip()
        except:
            get_flowUnit = None
        try:
            get_batchID = data["batchID"]
        except:
            get_batchID = None    



        Bulk_Weigths.objects.create(
            weightID = get_weightID,
            dateTime = formatted_date,
            opType = get_opType,
            terminal = get_terminal,
            net = get_net,
            tare = get_tare,
            wtUnit = get_wtUnit,
            stepNumber = get_stepNumber,
            subtotNumber = get_subtotNumber,
            prodNumber = get_prodNumber,
            stepTotal = get_stepTotal,
            subtotTotal = get_subtotTotal,
            prodTotal = get_prodTotal,
            grandTotal = get_grandTotal,
            flow = get_flow,
            flowUnit = get_flowUnit,
            batchID = get_batchID,


        )
        return JsonResponse({"message": "Lote not found on Database!"})

# @csrf_exempt
# @require_http_methods(['POST'])
# def lote_create_dinamic(request):
#     if request.body:
#         data = json.loads(request.body)
#         print(data)
#         ext_data={}

#         for key, value in data.items():
#             ext_data[key] = value
            
#         for item, valor in ext_data.items():
#             print(item, '=',valor,)

    
#         Lote.objects.create(
#             batch = get_lote,
#             production_date =  get_production_date,
#             terminal = get_terminal,
#             sequencial = get_terminal,
#             type = get_type,
#             liquid = get_liquid,
#             tara = get_tara,
#             unit_of_measurement = get_unit_of_measurement,
#             client = get_client,
#             product_number = get_product_number,
#             product_name = get_product_name,
#             sub_total = get_sub_total,
#             total = get_total,
#             message = get_message,
#         )
#         return JsonResponse({"message": "Lote not found on Database!"})