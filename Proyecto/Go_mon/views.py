from datetime import date, datetime
import calendar
from django.shortcuts import render, redirect
from .models import Comuna,Dia, Dia_Bloq,Bloque, Direc_Apoderado, Direc_Cuidador, Habil_cuid, Habilidad, Idio_cuid, Idioma, Region, Servi_Bloq, Servicio, Sexo, Apoderado, Cuidador, Menor, Usuario, Rol
from django.contrib import messages
from django.contrib.auth import logout

def Pag_Principal(request):
    return render(request,'Go_mon/Pag_Principal.html')

def iniciouser(request):
    return render(request,'Go_mon/iniciouser.html')

def inicioadmin(request):
    return render(request,'Go_mon/inicioadmin.html')

def Historial_evaluacion(request):
    aa = Apoderado.objects.all()
    contexto = {"datos": aa}
    return render(request,'Go_mon/Historial_evaluacion.html', contexto)

def adm(request):
    return render(request,'Go_mon/adm.html')

def perfcuidador1(request):
    return render(request,'Go_mon/perfcuidador1.html')

def mod_perfil(request):
    return render(request,'Go_mon/mod_perfil.html')

def admbanear(request):
    return render(request,'Go_mon/admbanear.html')

def admministrador(request):
    return render(request,'Go_mon/administrador.html')

def buscador(request):
    return render(request,'Go_mon/buscador.html')

def cambio(request):
    return render(request,'Go_mon/cambio.html')

def Apoderado_perfil(request):
    return render(request,'Go_mon/Apoderado_perfil.html')

def perfil_editar(request):
    return render(request,'Go_mon/perfil_editar.html')

def recerva(request):
    return render(request,'Go_mon/recerva.html')

def listarroles(request):
    roles = Rol.objects.all()
    contexto = {"qroles":roles}
    return render(request,'Go_mon/registro.html',contexto)

def registro(request):
    email=request.POST['email']
    passw=request.POST['cont']
    esta="si"
    rut=request.POST['rut']
    rol=request.POST['elrol']
    rol2=Rol.objects.get(id_Rol = rol)

    try:
        if Usuario.objects.filter(rut=rut).exists():
            messages.add_message(request=request, level=messages.SUCCESS, message="Usted ya se encuentra registrado, inicie sesion")
            return redirect('iniciouser')
        elif Usuario.objects.filter(correo=email).exists():
            messages.add_message(request=request, level=messages.SUCCESS, message="Este correo ya se encuentra registrado, inicie sesion")
            return redirect('iniciouser')
        else:
            Usuario.objects.create(correo = email, clave = passw, estatus = esta, rut = rut, rol=rol2)
            x = Usuario.objects.get(correo = email, clave = passw, rut = rut) 
            num_rol = Rol.objects.get(nombre = "Apoderado")
            sexos = Sexo.objects.all()
            if x.rol == num_rol:
                contexto = {"usuario_apo": x,"lista_sexos":sexos}
                return render(request,'Go_mon/registro_apo.html',contexto)
            else: 
                contexto = {"usuario": x, "lista_sexos":sexos}
                return render(request,'Go_mon/registro_cui.html',contexto)
    except Usuario.MultipleObjectsReturned:
        messages.add_message(request=request, level=messages.SUCCESS, message="vuelva a intentar")
        return redirect('Pag_Principal')   


def registrar_apoderado(request):
    rutapo=request.POST['rut']
    nombapo=request.POST['nomb']
    papelliapo=request.POST['Ap']
    sapelliapo=request.POST['Ap2']
    tefapo=request.POST['telefo']
    emailapo=request.POST['email']
    fotoapo=request.FILES['foto1']
    sexoapo=request.POST['sex1']
    sexoapo2=Sexo.objects.get(id_Sexo = sexoapo)
    
    Apoderado.objects.create(rut_apoderado = rutapo, nombre = nombapo, p_apellido = papelliapo,
    s_apellido = sapelliapo, correo = emailapo, celular = tefapo, foto = fotoapo, sexo = sexoapo2)
    
    comunas = Comuna.objects.all()
    regiones = Region.objects.all()
    buscandoapoderado = Apoderado.objects.get(rut_apoderado = rutapo) 
    contexto = {"ap":buscandoapoderado, "comuapo":comunas, "regiapo":regiones}
    return render(request,'Go_mon/direccion_apo.html',contexto)

def registrar_dir(request):
    rutapo= request.POST['rut']
    direcapo = request.POST['direc']
    dptoapo = request.POST['dpto']
    comuapo=request.POST['comunas']
    comuapo2=Comuna.objects.get(id_Comuna = comuapo)

    rut4 = Apoderado.objects.get(rut_apoderado = rutapo)
    Direc_Apoderado.objects.create(rut_apoderado = rut4, descripApoderado = direcapo, 
    deptoApoderado=dptoapo, comuna = comuapo2)  
    return redirect('Pag_Principal')  


def registrar_cuidador(request):
    rutcui=request.POST['rut']
    nombcui=request.POST['nomb']
    papellicui=request.POST['Ap']
    sapellicui=request.POST['Ap2']
    tefcui=request.POST['telefo']
    emailcui=request.POST['email']
    fotocui=request.FILES['Image']
    sexocui=request.POST['sex1']
    sexocui2=Sexo.objects.get(id_Sexo = sexocui)
    fecnaccui=request.POST['nacim']
    desccui=request.POST['descrip']
    expcui=request.POST['exp']
    tarifacui=request.POST['tarifa']
    enlacecui=request.POST['recording']

    Cuidador.objects.create(rut_cuidador = rutcui, nombre = nombcui, p_apellido = papellicui,
    s_apellido = sapellicui, correo = emailcui, celular = tefcui, foto = fotocui, sexo = sexocui2,
    fNacimiento = fecnaccui, descripcion = desccui, tiempo_exp_lab = expcui, tarifa = tarifacui, 
    enlace_video = enlacecui)
     
    comunas = Comuna.objects.all()
    regiones = Region.objects.all()
    buscandocuidador = Cuidador.objects.get(rut_cuidador = rutcui)
    contexto = {"cui":buscandocuidador, "comuapo":comunas, "regiapo":regiones}
    return render(request,'Go_mon/direccion_cui.html',contexto)


def registrar_dircui(request):
    rutcui= request.POST['rut']
    direccui = request.POST['direc']
    dptocui = request.POST['dpto']
    comucui=request.POST['comunas']
    comucui2=Comuna.objects.get(id_Comuna = comucui)
    rut2 = Cuidador.objects.get(rut_cuidador = rutcui)

    Direc_Cuidador.objects.create(rut_cuidador = rut2, descripCuidador = direccui, 
    deptoCuidador=dptocui, comuna = comucui2)  
    idiomas = Idioma.objects.all()
    buscando = Cuidador.objects.get(rut_cuidador = rutcui)
    contexto = {"cui":buscando, "idioma":idiomas}
    return render(request,'Go_mon/descripcion.html',contexto)

def ingresaidioma(request):
    rutcui= request.POST['rut']
    rutcui2=Cuidador.objects.get(rut_cuidador = rutcui)
    idiomacui=request.POST['myidioma']
    idiomacui2=Idioma.objects.get(id_idioma = idiomacui)

    Idio_cuid.objects.create(rut_cuidador = rutcui2, idioma = idiomacui2)
    idiomas = Idioma.objects.all()
    idiomasselect = Idio_cuid.objects.filter(rut_cuidador = rutcui2)
    return render(request,'Go_mon/descripcion.html',{"cui":rutcui2, "idioma":idiomas, "idiomarut":idiomasselect}) 

def habilidades(request):
    rutcui= request.POST['rut']
    rutcui2=Cuidador.objects.get(rut_cuidador = rutcui)

    fumacui = request.POST['fuma']
    hijocui = request.POST['hijo']
    carnetcui = request.POST['carnet']
    autocui = request.POST['auto']
    especialcui = request.POST['especial']
    titulocui = request.POST['titulo']
    auxcui = request.POST['aux']
    cocinacui = request.POST['cocina']
    tareacui = request.POST['tarea']
    mascotacui = request.POST['mascota']
    ninocui = request.POST['nino']
    manualidadcui = request.POST['manualidad']
    leercui = request.POST['leer']
    
    if fumacui == "1":
        fumacui2=Habilidad.objects.get(id_habilidad = fumacui)
        Habil_cuid.objects.create(rut_cuidador = rutcui2, id_habilidad = fumacui2)

    if hijocui == "3":
        hijocui2=Habilidad.objects.get(id_habilidad = hijocui)
        Habil_cuid.objects.create(rut_cuidador = rutcui2, id_habilidad = hijocui2)

    if carnetcui == "2":
        carnetcui2=Habilidad.objects.get(id_habilidad = carnetcui)
        Habil_cuid.objects.create(rut_cuidador = rutcui2, id_habilidad = carnetcui2)

    if autocui == "4":
        autocui2=Habilidad.objects.get(id_habilidad = autocui)
        Habil_cuid.objects.create(rut_cuidador = rutcui2, id_habilidad = autocui2)

    if especialcui == "5":
        especialcui2=Habilidad.objects.get(id_habilidad = especialcui)
        Habil_cuid.objects.create(rut_cuidador = rutcui2, id_habilidad = especialcui2)

    if titulocui == "6":
        titulocui2=Habilidad.objects.get(id_habilidad = titulocui)
        Habil_cuid.objects.create(rut_cuidador = rutcui2, id_habilidad = titulocui2)

    if auxcui == "7":
        auxcui2=Habilidad.objects.get(id_habilidad = auxcui)
        Habil_cuid.objects.create(rut_cuidador = rutcui2, id_habilidad = auxcui2)

    if cocinacui == "8":
        cocinacui2=Habilidad.objects.get(id_habilidad = cocinacui)
        Habil_cuid.objects.create(rut_cuidador = rutcui2, id_habilidad = cocinacui2)

    if tareacui == "9":
        tareacui2=Habilidad.objects.get(id_habilidad = tareacui)
        Habil_cuid.objects.create(rut_cuidador = rutcui2, id_habilidad = tareacui2)

    if mascotacui  == "11":
        mascotacui2=Habilidad.objects.get(id_habilidad = mascotacui)
        Habil_cuid.objects.create(rut_cuidador = rutcui2, id_habilidad = mascotacui2)

    if ninocui == "10":
        ninocui2=Habilidad.objects.get(id_habilidad = ninocui)
        Habil_cuid.objects.create(rut_cuidador = rutcui2, id_habilidad = ninocui2)


    if manualidadcui == "12":
        manualidadcui2=Habilidad.objects.get(id_habilidad = manualidadcui)
        Habil_cuid.objects.create(rut_cuidador = rutcui2, id_habilidad = manualidadcui2)


    if leercui == "13":
        leercui2=Habilidad.objects.get(id_habilidad = leercui)
        Habil_cuid.objects.create(rut_cuidador = rutcui2, id_habilidad = leercui2)
    
    return render(request,'Go_mon/Pag_Principal.html',{"cui":rutcui2})

def modificar_cuidador(request, rut):
    cuidador1 = Cuidador.objects.get(rut_cuidador = rut) # obtengo los datos del cuidador 
    direccion = Direc_Cuidador.objects.get(rut_cuidador = rut)
    com = Comuna.objects.all()
    servicioCui = Servicio.objects.filter(rut_cuidador = cuidador1)
    contexto = {"c" : cuidador1, "d":direccion, "com":com, "sercui":servicioCui}
    return render(request,'go_mon/mod_perfil.html',contexto)

def modificarCui(request):
    rutCui = request.POST['rut']
    nombreCui = request.POST['nombre']
    primerCui = request.POST['ap']
    segundoCui = request.POST['ap2']
    correoCui = request.POST['email']
    telfCui = request.POST['cel']
    direcCui = request.POST['direc']
    comuCui = request.POST['comuna']
    print("1")

    cuidador = Cuidador.objects.get(rut_cuidador = rutCui) #el registro original
    #comienzo a reemplazar los valores en ese registro original
    cuidador.nombre = nombreCui
    cuidador.p_apellido = primerCui
    cuidador.s_apellido = segundoCui
    cuidador.correo = correoCui
    cuidador.celular = telfCui
    cuidador.save() #update

    x = Usuario.objects.get(rut = rutCui)
    x.correo = correoCui
    x.save()

    comuCui2 = Comuna.objects.get(id_Comuna=comuCui)

    direc = Direc_Cuidador.objects.get(rut_cuidador = rutCui)
    direc.descripCuidador = direcCui
    direc.comuna = comuCui2
    direc.save()
    print("4")

    sexos = Sexo.objects.all()
    cuidador= Cuidador.objects.get(rut_cuidador = x.rut)
    direccion = Direc_Cuidador.objects.get(rut_cuidador = x.rut)
    servicioCui = Servicio.objects.filter(rut_cuidador = cuidador)
    contexto ={"c": cuidador, "d":direccion, "x" : x, "sercui":servicioCui}
    return render(request,'Go_mon/perfil.html',contexto)

def inicio_sesion(request):
    cor = request.POST['correoU']
    cont = request.POST['pass']
    
    try:
        x = Usuario.objects.get(correo = cor, clave = cont)
        rol2 = Rol.objects.get(nombre = "Apoderado")

        sexos = Sexo.objects.all()
        if x.rol == rol2:
            aa= Apoderado.objects.get(rut_apoderado = x.rut)
            da= Direc_Apoderado.objects.get(rut_apoderado = x.rut)
            hijoselect = Menor.objects.filter(rut_apoderado = aa)
            print("1")
            servicioApo = Servicio.objects.filter(rut_apoderado = aa)
            print("2")
            Servi_BloqApo = Servi_Bloq.objects.filter(id_Sb = servicioApo)
            print("3")
            contexto ={"apoderado": x,"datos": aa,"direc":da, "sexomen":sexos,"hijo":hijoselect, "serapo":servicioApo, "diabloq":Servi_BloqApo}
            return render(request,'Go_mon/Apoderado_perfil.html',contexto)
        else:
            cuidador= Cuidador.objects.get(rut_cuidador = x.rut)
            direccion = Direc_Cuidador.objects.get(rut_cuidador = x.rut)
            servicioCui = Servicio.objects.filter(rut_cuidador = cuidador)
            x = Usuario.objects.get(rut = x.rut)
            contexto ={"c": cuidador, "d":direccion, "x" : x, "sercui":servicioCui}
            return render(request,'Go_mon/perfil.html',contexto)
    except Usuario.DoesNotExist:
        messages.add_message(request=request, level=messages.SUCCESS, message="Clave y(o)Clave incorrecta")
        return redirect('iniciouser')

def buscarcomuna (request, rut):
    aa = Apoderado.objects.get(rut_apoderado = rut)
    da= Direc_Apoderado.objects.get(rut_apoderado = rut)
    x = Usuario.objects.get(rut = rut)
    comunabusq = request.POST['locality-input'] 
    comu = Comuna.objects.get(nombreComuna = comunabusq)
    ninera = Direc_Cuidador.objects.filter(comuna = comu)
    contexto ={"opninera":ninera, "datos": aa, "direc":da, "apoderado":x}
    return render(request,'Go_mon/Apoderado_perfil.html',contexto)

def modiA(request, rut):
    sex = Sexo.objects.all()
    aa = Apoderado.objects.get(rut_apoderado = rut)
    x = Usuario.objects.get(rut = rut)
    da= Direc_Apoderado.objects.get(rut_apoderado = aa)
    com = Comuna.objects.all()
    servicioApo = Servicio.objects.filter(rut_apoderado = aa)
    print("primero")

    contexto = {"sexo":sex, "apo":aa, "user":x, "di":da, "com":com, "serapo":servicioApo}
    return render(request,'Go_mon/modificar_apo.html',contexto)

def modifApo(request, rut):
    nom = request.POST['nombre']
    apa = request.POST['p_apellido']
    ama = request.POST['s_apellido']
    gen = request.POST['genero']
    tele = request.POST['telefono']
    mail = request.POST['email']
    direc = request.POST['direccion']
    comu = request.POST['comuna']
    rutA = request.POST['cedula']
    idD = request.POST['idDire']

    apo = Apoderado.objects.get(rut_apoderado = rutA)
    apo.nombre = nom
    apo.p_apellido = apa
    apo.s_apellido = ama

    sex2 = Sexo.objects.get(id_Sexo = gen)
    apo.sexo = sex2
    apo.celular = tele
    apo.correo = mail

    x = Usuario.objects.get(rut = rut)
    x.correo = mail
    x.save()

    dire = Direc_Apoderado.objects.get(id_DirApod = idD)
    dire.descripApoderado = direc
    comu2 = Comuna.objects.get(id_Comuna = comu)
    dire.comuna = comu2
    apo.save()
    dire.save()
    aa = Apoderado.objects.get(rut_apoderado = rut)
    x = Usuario.objects.get(rut = rut)
    hijoselect = Menor.objects.filter(rut_apoderado = aa)
    servicioApo = Servicio.objects.filter(rut_apoderado = aa)
    sexos = Sexo.objects.all()
    com = Comuna.objects.all()
    da= Direc_Apoderado.objects.get(rut_apoderado = aa)
    contexto ={"apoderado": x,"datos": aa,"direc":da, "sexomen":sexos,"hijo":hijoselect, "com":com, "serapo":servicioApo}
    return render(request,'Go_mon/Apoderado_perfil.html',contexto)

def registrar_menor(request):
    rutmen = request.POST['cedula']
    nombremen = request.POST['hijo']
    papmen = request.POST['pr_apellido']
    sapmen = request.POST['se_apellido']
    nacmen = request.POST['start']
    sexomen = request.POST['genero']
    rutApo = request.POST['rutApo']
    print("Registrar menor")
    rut1 = Apoderado.objects.get(rut_apoderado = rutApo)
    sexomen2=Sexo.objects.get(id_Sexo = sexomen)
    Menor.objects.create(rut_Menor = rutmen, nombre = nombremen, p_Apellido = papmen,
    s_Apellido = sapmen, fNacimiento = nacmen, sexo = sexomen2,rut_apoderado = rut1)

    aa= Apoderado.objects.get(rut_apoderado = rutApo)
    da= Direc_Apoderado.objects.get(rut_apoderado = rutApo)
    hijoselect = Menor.objects.filter(rut_apoderado = aa)
    sexos = Sexo.objects.all()
    servicioApo = Servicio.objects.filter(rut_apoderado = aa)
    x = Usuario.objects.get(rut = rutApo)
    print("2")
    contexto ={"apoderado": x,"datos": aa,"direc":da, "sexomen":sexos,"hijo":hijoselect, "serapo":servicioApo}
    return render(request,'Go_mon/Apoderado_perfil.html',contexto)

def elimHijo(request, id,rut):
    hijo = Menor.objects.get(rut_Menor = id)
    print("eliminar hijo")
    hijo.delete()
    print("2")
    aa = Apoderado.objects.get(rut_apoderado = rut)
    x = Usuario.objects.get(rut = rut)
    hijoselect = Menor.objects.filter(rut_apoderado = aa)
    servicioApo = Servicio.objects.filter(rut_apoderado = aa)
    sexos = Sexo.objects.all()
    da= Direc_Apoderado.objects.get(rut_apoderado = aa)
    contexto ={"apoderado": x,"datos": aa,"direc":da, "sexomen":sexos,"hijo":hijoselect, "serapo":servicioApo}
    return render(request,'Go_mon/Apoderado_perfil.html',contexto)

def salir(request):
    logout(request)
    return redirect('Pag_Principal')

def modiMenor(request, id, rut):
    men = Menor.objects.get(rut_Menor = id)
    sex = Sexo.objects.all()
    aa = Apoderado.objects.get(rut_apoderado = rut)
    x = Usuario.objects.get(rut = rut)
    servicioApo = Servicio.objects.filter(rut_apoderado = aa)
    print("primero")

    contexto = {"menor":men, "sexo":sex, "apo":aa, "user":x, "serapo":servicioApo}
    return render(request,'Go_mon/modificar_menor.html',contexto)

def modif(request, id, rut):
    rutm = request.POST['cedula']
    nomb = request.POST['hijo']
    apaterno = request.POST['pr_apellido']
    amaterno = request.POST['se_apellido']
    fenac = request.POST['start']
    gen = request.POST['genero']
    
    hijo = Menor.objects.get(rut_Menor = rutm)
    hijo.nombre = nomb
    hijo.p_Apellido = apaterno
    hijo.s_Apellido = amaterno
    hijo.fNacimiento = fenac

    gen2 = Sexo.objects.get(id_Sexo = gen)
    hijo.sexo = gen2
    hijo.save()
    print("segundo")
    aa = Apoderado.objects.get(rut_apoderado = rut)
    x = Usuario.objects.get(rut = rut)
    hijoselect = Menor.objects.filter(rut_apoderado = aa)
    sexos = Sexo.objects.all()
    servicioApo = Servicio.objects.filter(rut_apoderado = aa)
    da= Direc_Apoderado.objects.get(rut_apoderado = aa)
    contexto ={"apoderado": x,"datos": aa,"direc":da, "sexomen":sexos,"hijo":hijoselect, "serapo":servicioApo}
    return render(request,'Go_mon/Apoderado_perfil.html',contexto)

def volapo(request, rut):
    aa = Apoderado.objects.get(rut_apoderado = rut)
    x = Usuario.objects.get(rut = rut)
    hijoselect = Menor.objects.filter(rut_apoderado = aa)
    sexos = Sexo.objects.all()
    cuid = Cuidador.objects.all()
    da= Direc_Apoderado.objects.get(rut_apoderado = aa)
    contexto ={"apoderado": x,"datos": aa,"direc":da, "sexomen":sexos,"hijo":hijoselect, "opninera":cuid}
    return render(request,'Go_mon/Apoderado_perfil.html',contexto)

def mapa(request, rut, rutap):
    cui = Cuidador.objects.get(rut_cuidador = rut)
    aa = Apoderado.objects.get(rut_apoderado = rutap)
    x = Usuario.objects.get(rut = rut)
    contexto = {"m" : cui, "cuidador":x, "datos": aa}
    return render(request,'Go_mon/perfcuidador1.html',contexto)

def defrecerva(request, rut, rutap):
    cui = Cuidador.objects.get(rut_cuidador = rut)
    aa = Apoderado.objects.get(rut_apoderado = rutap)
    x = Usuario.objects.get(rut = rut)
    contexto = {"m" : cui, "cuidador":x, "datos": aa}
    return render(request,'Go_mon/recerva.html',contexto)

def volcui(request, rut):
    cui = Cuidador.objects.get(rut_cuidador = rut)
    x = Usuario.objects.get(rut = rut)
    da= Direc_Cuidador.objects.get(rut_cuidador = cui)
    contexto ={"cuidador": x,"c": cui,"d":da}
    return render(request,'Go_mon/perfil.html',contexto)

def servicui(request, rut, rutap):
    cui = Cuidador.objects.get(rut_cuidador = rut)
    aa = Apoderado.objects.get(rut_apoderado = rutap)
    x = Usuario.objects.get(rut = rut)
    da= Direc_Cuidador.objects.get(rut_cuidador = cui)
    conta = 0
    hoy=request.POST['fecha']
    fecha=request.POST['fecha']
    fecha_dt = datetime.strptime(fecha, '%Y-%m-%d')
    print(calendar.day_name[fecha_dt.weekday()])
    dia = calendar.day_name[fecha_dt.weekday()]
    texto = ""
    if dia == "Monday":
        texto="Lunes"
    elif dia == "Tuesday":
        texto = "Martes"
    elif dia == "Wednesday":
        texto = "Miercoles"
    elif dia == "Thursday":
        texto = "Jueves"
    elif dia == "Friday":
        texto = "Viernes"
    elif dia == "Saturday":
        texto = "Sabado"
    else: 
        texto = "Domingo"

    precio=request.POST['tarif']
    esta="si"
    if(request.POST.get('c1')):
        conta = conta + 1
    if(request.POST.get('c2')):
        conta = conta + 1
    if(request.POST.get('c3')):
        conta = conta + 1
    if(request.POST.get('c4')):
        conta = conta + 1
    if(request.POST.get('c5')):
        conta = conta + 1
    if(request.POST.get('c6')):
        conta = conta + 1
    if(request.POST.get('c7')):
        conta = conta + 1
    if(request.POST.get('c8')):
        conta = conta + 1
    if(request.POST.get('c9')):
        conta = conta + 1
    if(request.POST.get('c10')):
        conta = conta + 1
    if(request.POST.get('c11')):
        conta = conta + 1
    if(request.POST.get('c12')):
        conta = conta + 1
    if(request.POST.get('c13')):
        conta = conta + 1
    if(request.POST.get('c14')):
        conta = conta + 1
    if(request.POST.get('c15')):
        conta = conta + 1
    if(request.POST.get('c16')):
        conta = conta + 1

    serv = Servicio.objects.create(fContrato = hoy, fInicio = fecha, fFinal = fecha, estatus=esta, 
    costoH = precio, cantidadH = conta, rut_apoderado = aa, rut_cuidador = cui)
    if(request.POST.get('c1')):
        id_dia = Dia.objects.get(nombreDia = texto)
        print(id_dia)
        id_bloque = Bloque.objects.get(hora = "08:00 - 08:50")
        print(id_bloque)
        id_dia_bloque = Dia_Bloq.objects.get(Dia = id_dia, bloque = id_bloque)
        Servi_Bloq.objects.create(id_Db = id_dia_bloque, servicio = serv)
    if(request.POST.get('c2')):
        id_dia = Dia.objects.get(nombreDia = texto)
        id_bloque = Bloque.objects.get(hora = "09:00 - 09:50")
        id_dia_bloque = Dia_Bloq.objects.get(Dia = id_dia, bloque = id_bloque)
        Servi_Bloq.objects.create(id_Db = id_dia_bloque, servicio = serv)
    if(request.POST.get('c3')):
        id_dia = Dia.objects.get(nombreDia = texto)
        id_bloque = Bloque.objects.get(hora = "10:00 - 10:50")
        id_dia_bloque = Dia_Bloq.objects.get(Dia = id_dia, bloque = id_bloque)
        Servi_Bloq.objects.create(id_Db = id_dia_bloque, servicio = serv)
    if(request.POST.get('c4')):
        id_dia = Dia.objects.get(nombreDia = texto)
        id_bloque = Bloque.objects.get(hora = "11:00 - 11:50")
        id_dia_bloque = Dia_Bloq.objects.get(Dia = id_dia, bloque = id_bloque)
        Servi_Bloq.objects.create(id_Db = id_dia_bloque, servicio = serv)
    if(request.POST.get('c5')):
        id_dia = Dia.objects.get(nombreDia = texto)
        id_bloque = Bloque.objects.get(hora = "12:00 - 12:50")
        id_dia_bloque = Dia_Bloq.objects.get(Dia = id_dia, bloque = id_bloque)
        Servi_Bloq.objects.create(id_Db = id_dia_bloque, servicio = serv)
    if(request.POST.get('c6')):
        id_dia = Dia.objects.get(nombreDia = texto)
        id_bloque = Bloque.objects.get(hora = "13:00 - 13:50")
        id_dia_bloque = Dia_Bloq.objects.get(Dia = id_dia, bloque = id_bloque)
        Servi_Bloq.objects.create(id_Db = id_dia_bloque, servicio = serv)
    if(request.POST.get('c7')):
        id_dia = Dia.objects.get(nombreDia = texto)
        id_bloque = Bloque.objects.get(hora = "14:00 - 14:50")
        id_dia_bloque = Dia_Bloq.objects.get(Dia = id_dia, bloque = id_bloque)
        Servi_Bloq.objects.create(id_Db = id_dia_bloque, servicio = serv)
    if(request.POST.get('c8')):
        id_dia = Dia.objects.get(nombreDia = texto)
        id_bloque = Bloque.objects.get(hora = "15:00 - 15:50")
        id_dia_bloque = Dia_Bloq.objects.get(Dia = id_dia, bloque = id_bloque)
        Servi_Bloq.objects.create(id_Db = id_dia_bloque, servicio = serv)
    if(request.POST.get('c9')):
        id_dia = Dia.objects.get(nombreDia = texto)
        id_bloque = Bloque.objects.get(hora = "16:00 - 16:50")
        id_dia_bloque = Dia_Bloq.objects.get(Dia = id_dia, bloque = id_bloque)
        Servi_Bloq.objects.create(id_Db = id_dia_bloque, servicio = serv)
    if(request.POST.get('c10')):
        id_dia = Dia.objects.get(nombreDia = texto)
        id_bloque = Bloque.objects.get(hora = "17:00 - 17:50")
        id_dia_bloque = Dia_Bloq.objects.get(Dia = id_dia, bloque = id_bloque)
        Servi_Bloq.objects.create(id_Db = id_dia_bloque, servicio = serv)
    if(request.POST.get('c11')):
        id_dia = Dia.objects.get(nombreDia = texto)
        id_bloque = Bloque.objects.get(hora = "18:00 - 18:50")
        id_dia_bloque = Dia_Bloq.objects.get(Dia = id_dia, bloque = id_bloque)
        Servi_Bloq.objects.create(id_Db = id_dia_bloque, servicio = serv)
    if(request.POST.get('c12')):
        id_dia = Dia.objects.get(nombreDia = texto)
        id_bloque = Bloque.objects.get(hora = "19:00 - 19:50")
        id_dia_bloque = Dia_Bloq.objects.get(Dia = id_dia, bloque = id_bloque)
        Servi_Bloq.objects.create(id_Db = id_dia_bloque, servicio = serv)
    if(request.POST.get('c13')):
        id_dia = Dia.objects.get(nombreDia = texto)
        id_bloque = Bloque.objects.get(hora = "20:00 - 20:50")
        id_dia_bloque = Dia_Bloq.objects.get(Dia = id_dia, bloque = id_bloque)
        Servi_Bloq.objects.create(id_Db = id_dia_bloque, servicio = serv)
    if(request.POST.get('c14')):
        id_dia = Dia.objects.get(nombreDia = texto)
        id_bloque = Bloque.objects.get(hora = "21:00 - 21:50")
        id_dia_bloque = Dia_Bloq.objects.get(Dia = id_dia, bloque = id_bloque)
        Servi_Bloq.objects.create(id_Db = id_dia_bloque, servicio = serv)
    if(request.POST.get('c15')):
        id_dia = Dia.objects.get(nombreDia = texto)
        id_bloque = Bloque.objects.get(hora = "22:00 - 22:50")
        id_dia_bloque = Dia_Bloq.objects.get(Dia = id_dia, bloque = id_bloque)
        Servi_Bloq.objects.create(id_Db = id_dia_bloque, servicio = serv)
    if(request.POST.get('c16')):
        id_dia = Dia.objects.get(nombreDia = texto)
        id_bloque = Bloque.objects.get(hora = "23:00 - 23:50")
        id_dia_bloque = Dia_Bloq.objects.get(Dia = id_dia, bloque = id_bloque)
        Servi_Bloq.objects.create(id_Db = id_dia_bloque, servicio = serv)

    hijoselect = Menor.objects.filter(rut_apoderado = aa)
    y = Usuario.objects.get(rut = rutap)
    da= Direc_Apoderado.objects.get(rut_apoderado = aa)
    servicioApo = Servicio.objects.filter(rut_apoderado = aa)
    sexos = Sexo.objects.all()

    contexto ={"cuidador": x,"c": cui,"d":da, "datos": aa, "direc":da, "apoderado": y, "hijo":hijoselect, "serapo":servicioApo, "sexomen":sexos}
    return render(request,'Go_mon/Apoderado_perfil.html',contexto)