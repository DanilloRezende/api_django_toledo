import json
from datetime import date, datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from backend.core.forms import LoteForm
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
        get_lote = data["batch"]
        get_production_date = data["production_date"]
        formatted_date = datetime.strptime(get_production_date, '%b %d %Y %I:%M%p' ).strftime('%d/%m/%Y')
        get_terminal = data["terminal"]
        get_sequencial = data["sequencial"]
        get_type = str(data["type"]).rstrip()
        get_liquid = float(data["liquid"])
        get_tara = float(data["tara"])
        get_unit_of_measurement = str(data["unit_of_measurement"]).rstrip()
        get_client = str(data["client"]).rstrip()
        get_product_number = int(data["product_number"])
        get_product_name = str(data["product_name"]).rstrip()
        get_sub_total = float(data["sub_total"])
        get_total = float(data["total"])
        get_message = str(data["message"]).rstrip()


        Lote.objects.create(
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
        get_eventID = data["eventID"]
        get_terminal = data["terminal"]
        get_dateTime = data["dateTime"]
        formatted_date = datetime.strptime(get_dateTime, '%b %d %Y %I:%M%p' ).strftime('%d/%m/%Y')
        get_evtType = data["evtType"]
        get_evtCode = data["evtCode"]
        get_evtMessage = str(data["evtMessage"]).rstrip()
        
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
        get_terminal = data["terminal"]
        get_batchStatus = data["batchStatus"]
        get_userField1 = str(data["userField1"]).rstrip()
        get_userField2 = str(data["userField2"]).rstrip()
        get_userField3 = str(data["userField3"]).rstrip()
        get_userField4 = str(data["userField4"]).rstrip()
        get_userField5 = str(data["userField5"]).rstrip()
        get_userField6 = str(data["userField6"]).rstrip()
        get_prodNumberList = str(data["prodNumberList"]).rstrip()
        get_subtotNumberList = str(data["subtotNumberList"]).rstrip()
        get_targetValueList = str(data["targetValueList"]).rstrip()
       


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
        get_weightID = data["weightID"]
        get_dateTime = data["dateTime"]
        formatted_date = datetime.strptime(get_dateTime, '%b %d %Y %I:%M%p' ).strftime('%d/%m/%Y')
        get_opType = data["opType"]
        get_terminal = str(data["terminal"]).rstrip()
        get_net = float(data["net"])
        get_tare = str(data["tare"]).rstrip()
        get_wtUnit = str(data["wtUnit"]).rstrip()
        get_stepNumber = str(data["stepNumber"]).rstrip()
        get_subtotNumber = str(data["subtotNumber"]).rstrip()
        get_prodNumber = str(data["prodNumber"]).rstrip()
        get_stepTotal = float(data["stepTotal"])
        get_subtotTotal = str(data["subtotTotal"]).rstrip()
        get_prodTotal = float(data["prodTotal"])
        get_grandTotal = float(data["grandTotal"])
        get_flow = float(data["flow"])
        get_flowUnit = str(data["flowUnit"]).rstrip()
        get_batchID = str(data["batchID"]).rstrip()
       


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