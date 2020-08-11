from request_api import *
from connection import Conn
from pymongo import MongoClient
from pprint import pprint
import bson
import time
from datetime import timedelta, datetime

class updateData():
    def insertUpdateData():      
        # Menghitung Waktu
        mulai = time.time()
        
        # Variabel untuk menampung data sementara
        update1, update2, update3, update4, update5, update6, update7, update8, update9, update10, update11 = [],[],[],[],[],[],[],[],[],[],[]
        login, login_password, login_username = [],[],[]
        dcerpcrequest, dcerpcrequest_opnum, dcerpcrequest_uuid = [],[],[]
        dcerpcbind, dcerpcbind_transfersyntax, dcerpcrequest_uuid = [],[],[]
        offer, offer_url = [],[]
        download, download_url, download_md5_hash = [],[],[]
        mssql_command, mssql_command_cmd, mssql_command_status = [],[],[]
        mssql_fingerprint, mssql_fingerprint_hostname, mssql_fingerprint_appname, mssql_fingerprint_cltintname = [],[],[],[]
        mysql_command, mysql_command_arg, mysql_command_arg_data, mysql_command_arg_index = [],[],[],[]
        mysql_command_cmd, mysql_command_op, mysql_command_op_name  = [],[],[]
        null = None

        # Mendapatkan panjang respon dari masing masing tabel
        respon1, respon2 = len(get_respon1()), len(get_respon2())
        respon3, respon4 = len(get_respon3()), len(get_respon4())
        respon5, respon6 = len(get_respon5()), len(get_respon6())
        respon7, respon8 = len(get_respon7()), len(get_respon8())
        respon9, respon10, respon11 = len(get_respon9()), len(get_respon10()), len(get_respon11())
        
        print("Jumlah Koneksi Terbaru : {}".format(respon1))
        
        # Memasukkan data ke dalam variabel sementara
        if respon1 > 0 :
            for a in get_respon1(): 
                update1.append(a)
            # Menghapus data agar penyimpanan di Raspberry menjadi lebih ringkas
            get_respon1_delete()
        if respon2 > 0:
            for b in get_respon2(): 
                update2.append(b)
            get_respon2_delete()    
        if respon3 > 0:
            for c in get_respon3(): 
                update3.append(c)
            get_respon3_delete()    
        if respon4 > 0:
            for d in get_respon4(): 
                update4.append(d)
            get_respon4_delete()    
        if respon5 > 0:
            for e in get_respon5(): 
                update5.append(e)
            get_respon5_delete()    
        if respon6 > 0:
            for f in get_respon6(): 
                update6.append(f)
            get_respon6_delete()    
        if respon7 > 0:
            for g in get_respon7(): 
                update7.append(g)
            get_respon7_delete()    
        if respon8 > 0:
            for h in get_respon8(): 
                update8.append(h)
            get_respon8_delete()    
        if respon9 > 0:
            for i in get_respon9(): 
                update9.append(i)
            get_respon9_delete()    
        if respon10 > 0:
            for j in get_respon10(): 
                update10.append(j)
            get_respon10_delete()    
        if respon11 > 0:
            for k in get_respon11(): 
                update11.append(k)
            get_respon11_delete()    
        
        # Melakukan ekstrak data dari variabel sementara
        for hasil1 in update1:
            connection1 = hasil1['connection']
            connection2 = hasil1['connection_type']
            connection3 = hasil1['connection_transport']
            connection4 = hasil1['connection_protocol']
            connection5 = hasil1['connection_timestamp']
            connection6 = hasil1['connection_root']
            connection7 = hasil1['connection_parent']
            connection8 = hasil1['local_host']
            connection9 = hasil1['local_port']
            connection10 = hasil1['remote_host']
            connection11 = hasil1['remote_hostname']
            connection12 = hasil1['remote_port']
            for hasil2 in update2:
                # Melakukan pencocokan antara tabel Connections dan Logins 
                if (hasil2['connection'] == connection1):
                    login = hasil2['login']
                    login_password = hasil2['login_password']
                    login_username = hasil2['login_username']
                    break
                # Jika tidak ada, maka isi dengan None
                else:
                    login = None
                    login_password = None
                    login_username = None
            

            # Mendefinisikan variabel sementara, karena tabel Dcerpcbinds dan Dcerpcrequests agak berbeda 
            # Khusus variabel sementara dcerpcbind didefinisikan disini, agar tidak mengambil total data dcerpcbind
            dcerpcrequest = []
            dcerpcrequest_opnum = []
            dcerpcrequest_uuid = []

            for hasil3 in update3:
                # Melakukan pencocokan antara tabel Connections dan Dcerpcrequests 
                if hasil3['connection'] == connection1:
                    dcerpcrequest.append(hasil3['dcerpcrequest'])
                    dcerpcrequest_opnum.append(hasil3['dcerpcrequest_opnum'])
                    dcerpcrequest_uuid.append(hasil3['dcerpcrequest_uuid'])
                # Tidak perlu diberikan else
            array_dcerpcrequests = []
            for i in range(0,len(dcerpcrequest)):
                doc = {
                    'dcerpcrequest' : dcerpcrequest[i],
                    'dcerpcrequest_opnum' : dcerpcrequest_opnum[i],
                    'dcerpcrequest_uuid' : dcerpcrequest_uuid[i]
                }
                array_dcerpcrequests.append(doc)
            
            dcerpcbind = []
            dcerpcbind_transfersyntax = []
            dcerpcbind_uuid = []

            for hasil4 in update4:
                # Melakukan pencocokan antara tabel Connections dan Dcerpcbinds
                if hasil4['connection'] == connection1:
                    dcerpcbind.append(hasil4['dcerpcbind'])
                    dcerpcbind_transfersyntax.append(hasil4['dcerpcbind_transfersyntax'])
                    dcerpcbind_uuid.append(hasil4['dcerpcbind_uuid'])
                # Tidak perlu diberikan else
            array_dcerpcbinds = []
            # Memasukkan semua data pada Dcerpcbinds ke dalam suatu Dokumen
            for i in range(0,len(dcerpcbind)):
                doc = {
                    'dcerpcbind' : dcerpcbind[i],
                    'dcerpcbind_transfersyntax' : dcerpcbind_transfersyntax[i],
                    'dcerpcbind_uuid' : dcerpcbind_uuid[i]
                }
                array_dcerpcbinds.append(doc)
                
            for hasil5 in update5:
                # Melakukan pencocokan antara tabel Connections dan Offers
                if (hasil5['connection'] == connection1):
                    offer = hasil5['offer']
                    offer_url = hasil5['offer_url']
                    break
                else:
                    offer = None
                    offer_url = None

            for hasil6 in update6:
                # Melakukan pencocokan antara tabel Connections dan Downloads
                if (hasil6['connection'] == connection1):
                    download = hasil6['download']
                    download_md5_hash = hasil6['download_md5_hash']
                    download_url = hasil6['download_url']
                    break
                else:
                    download = None
                    download_md5_hash = None
                    download_url = None

            for hasil7 in update7:
                # Melakukan pencocokan antara tabel Connections dan Mssql_Command
                if (hasil7['connection'] == connection1):
                    mssql_command = hasil7['mssql_command']
                    mssql_command_cmd = hasil7['mssql_command_cmd']
                    mssql_command_status = hasil7['mssql_command_status']
                    break
                else:
                    mssql_command = None
                    mssql_command_cmd = None
                    mssql_command_status = None

            for hasil8 in update8:
                # Melakukan pencocokan antara tabel Connections dan Mssql_Fingerprint
                if (hasil8['connection'] == connection1):
                    mssql_fingerprint = hasil8['mssql_fingerprint']
                    mssql_fingerprint_appname = hasil8['mssql_fingerprint_appname']
                    mssql_fingerprint_cltintname = hasil8['mssql_fingerprint_cltintname']
                    mssql_fingerprint_hostname = hasil8['mssql_fingerprint_hostname']
                    break
                else:
                    mssql_fingerprint = None
                    mssql_fingerprint_appname = None
                    mssql_fingerprint_cltintname = None
                    mssql_fingerprint_hostname = None
            
            for hasil9 in update9:
                # Melakukan pencocokan antara tabel Connections dan Mysql_Command
                if (hasil9['connection'] == connection1):
                    mysql_command = hasil9['mysql_command']
                    mysql_command_cmd = hasil9['mysql_command_cmd']
                    for hasil10 in update10:
                        # Melakukan pencocokan antara tabel Connections dan Mysql_Command_Arg
                        if (hasil10['mysql_command'] == mysql_command):
                            mysql_command_arg = hasil10['mysql_command_arg']
                            mysql_command_arg_data = hasil10['mysql_command_arg_data']
                            mysql_command_arg_index = hasil10['mysql_command_arg_index']
                            break
                        else:
                            mysql_command_arg = None
                            mysql_command_arg_data = None
                            mysql_command_arg_index = None
                    for hasil11 in update11:
                        # Melakukan pencocokan antara tabel Connections dan Mysql_Command_Cmd
                        if (hasil11['mysql_command_cmd'] == mysql_command_cmd):
                            mysql_command_op = hasil11['mysql_command_op']
                            mysql_command_op_name = hasil11['mysql_command_op_name']
                            break
                        else:
                            mysql_command_op = None
                            mysql_command_op_name = None
                    break  
                else:
                    mysql_command = None
                    mysql_command_cmd = None
            
            # Pembentukan Dokumen Embedded, memanggil setiap elemen variabel diatas
            Document = {
                '_id' : bson.ObjectId(),
                'connection': connection1,
                'connection_type' : connection2,
                'connection_transport' : connection3,
                'connection_protocol' : connection4,
                'connection_timestamp' : connection5,
                'connection_root' : connection6,
                'connection_parent' : connection7,
                'local_host' : connection8,
                'local_port' : connection9,
                'remote_host' : connection10,
                'remote_hostname' : connection11,
                'remote_port' : connection12,
                'logins' : [{
                    'login':login,
                    'login_password':login_password,
                    'login_username':login_username
                }],
                'dcerpcrequests' : array_dcerpcrequests,
                'dcerpcbinds' : array_dcerpcbinds,
                'offers' : [{
                    'offer' : offer,
                    'offer_url' : offer_url
                }],
                'downloads' : [{
                    'download' : download,
                    'download_md5_hash' : download_md5_hash,
                    'download_url' : download_url
                }],
                'mssql_commands' : [{
                    'mssql_command' : mssql_command,
                    'mssql_command_cmd' : mssql_command_cmd,
                    'mssql_command_status' : mssql_command_status
                }],
                'mssql_fingerprints' : [{
                    'mssql_fingerprint' : mssql_fingerprint,
                    'mssql_fingerprint_appname' : mssql_fingerprint_appname,
                    'mssql_fingerprint_cltintname' : mssql_fingerprint_cltintname,
                    'mssql_fingerprint_hostname' : mssql_fingerprint_hostname
                }],

                # VERSI_PISAH (jangan dihapus, untuk testing ketika VERSI GABUNG tidak berhasil)
                # 'mysql_commands' : [{
                #     'mysql_command': mysql_command,
                #     'mysql_command_cmd': mysql_command_cmd   
                # }],
                # 'mysql_command_args' : [{
                #     'mysql_command':mysql_command,
                #     'mysql_command_arg':mysql_command_arg,
                #     'mysql_command_arg_data_index':mysql_command_arg_index,
                #     'mysql_command_arg_data':mysql_command_arg_data
                # }],
                # 'mysql_command_ops' : [{
                #     'mysql_command_cmd':mysql_command_cmd,
                #     'mysql_command_op':mysql_command_op,
                #     'mysql_command_op_name':mysql_command_op_name
                # }],
                # 'mysql_commands' : array_9,
                # 'mysql_command_args' : array_10,
                # 'mysql_command_ops' : array_11,
                # VERSI_GABUNG
                'mysql_details' : [{
                    'mysql_command': mysql_command,
                    'mysql_command_arg':mysql_command_arg,
                    'mysql_command_arg_data_index':mysql_command_arg_index,
                    'mysql_command_arg_data':mysql_command_arg_data},
                    {
                    'mysql_command_cmd': mysql_command_cmd,
                    'mysql_command_op':mysql_command_op,
                    'mysql_command_op_name':mysql_command_op_name
                }]
            }
            # Memasukkan ke dalam Database bernama embedded
            Conn().db.embedded.insert_one(Document)
        
        # Menghapus data yang bernilai STRING KOSONG, NULL, dan ARRAY KOSONG
        for null_array_string in Conn().db.embedded.find():
            Conn().db.embedded.update_many( {'remote_hostname':''}, {'$unset':{'remote_hostname':0}} )
            Conn().db.embedded.update_many( {'connection_type':''},{'$unset':{'connection_type':0}} )
            Conn().db.embedded.update_many( {'connection_transport':''},{'$unset':{'connection_transport':0}} )
            Conn().db.embedded.update_many( {'connection_protocol':''},{'$unset':{'connection_protocol':0}} )
            Conn().db.embedded.update_many( {'connection_timestamp':''},{'$unset':{'connection_timestamp':0}} )
            Conn().db.embedded.update_many( {'connection_root':''},{'$unset':{'connection_root':0}} )
            Conn().db.embedded.update_many( {'connection_parent':''}, {'$unset':{'connection_parent':0}} )
            Conn().db.embedded.update_many( {'local_host':''},{'$unset':{'local_host':0}} )
            Conn().db.embedded.update_many( {'local_port':''},{'$unset':{'local_port':0}} )
            Conn().db.embedded.update_many( {'remote_host':''},{'$unset':{'remote_host':0}} )
            Conn().db.embedded.update_many( {'remote_hostname':''},{'$unset':{'remote_hostname':0}} )
            Conn().db.embedded.update_many( {'remote_port':''},{'$unset':{'remote_port':0}} )

            Conn().db.embedded.update_many( {'remote_hostname':null}, {'$unset':{'remote_hostname':0}} )
            Conn().db.embedded.update_many( {'connection_type':null},{'$unset':{'connection_type':0}} )
            Conn().db.embedded.update_many( {'connection_transport':null},{'$unset':{'connection_transport':0}} )
            Conn().db.embedded.update_many( {'connection_protocol':null},{'$unset':{'connection_protocol':0}} )
            Conn().db.embedded.update_many( {'connection_timestamp':null},{'$unset':{'connection_timestamp':0}} )
            Conn().db.embedded.update_many( {'connection_root':null},{'$unset':{'connection_root':0}} )
            Conn().db.embedded.update_many( {'connection_parent':null}, {'$unset':{'connection_parent':0}} )
            Conn().db.embedded.update_many( {'local_host':null},{'$unset':{'local_host':0}} )
            Conn().db.embedded.update_many( {'local_port':null},{'$unset':{'local_port':0}} )
            Conn().db.embedded.update_many( {'remote_host':null},{'$unset':{'remote_host':0}} )
            Conn().db.embedded.update_many( {'remote_hostname':null},{'$unset':{'remote_hostname':0}} )
            Conn().db.embedded.update_many( {'remote_port':null},{'$unset':{'remote_port':0}} )

            Conn().db.embedded.update_many( {'logins.login':{'$eq':null}}, {'$unset': {'logins':0}} )
            Conn().db.embedded.update_many( {"dcerpcrequests.dcerpcrequest":{'$eq':null}}, {'$unset': {"dcerpcrequests":0}} ) 
            Conn().db.embedded.update_many( {"dcerpcbinds":{'$eq':null}}, {'$unset': {"dcerpcbinds":0}} )
            Conn().db.embedded.update_many( {"offers.offer":{'$eq':null}}, {'$unset': {"offers":0}} )
            Conn().db.embedded.update_many( {"downloads.download":{'$eq':null}}, {'$unset': {"downloads":0}} )
            Conn().db.embedded.update_many( {"mssql_commands.mssql_command":{'$eq':null}}, {'$unset': {"mssql_commands":0}} )
            Conn().db.embedded.update_many( {"mssql_fingerprints.mssql_fingerprint":{'$eq':null}}, {'$unset': {"mssql_fingerprints":0}} ) 
            # VERSI_PISAH (jangan dihapus, untuk testing ketika VERSI GABUNG tidak berhasil)
            # Conn().db.embedded.update_many( {"mysql_commands.mysql_command" :{'$eq':null}}, {'$unset': {"mysql_commands":0}} )
            # Conn().db.embedded.update_many( {"mysql_command_args.mysql_command" :{'$eq':null}}, {'$unset': {"mysql_command_args":0}} )
            # Conn().db.embedded.update_many( {"mysql_command_ops.mysql_command_cmd" :{'$eq':null}}, {'$unset': {"mysql_command_ops":0}} )
            # VERSI_GABUNG
            Conn().db.embedded.update_many( {"mysql_details.mysql_command":{'$eq':null}}, {'$unset':{"mysql_details":0}} ) #VPS WORK
            # Conn().db.embedded.update_many({},{'$pull': {"mysql_details":{"mysql_command": {'$eq':null}} } },upsert=True) #PC WORK
            
            Conn().db.embedded.update_many( {'logins.login':{'$eq':[]}}, {'$unset': {'logins':0}} )
            Conn().db.embedded.update_many( {"dcerpcrequests.dcerpcrequest":{'$eq':[]}}, {'$unset': {"dcerpcrequests":0}} ) 
            Conn().db.embedded.update_many( {"dcerpcbinds":{'$eq':[]}}, {'$unset': {"dcerpcbinds":0}} )
            Conn().db.embedded.update_many( {"offers.offer":{'$eq':[]}}, {'$unset': {"offers":0}} )
            Conn().db.embedded.update_many( {"downloads.download":{'$eq':[]}}, {'$unset': {"downloads":0}} )
            Conn().db.embedded.update_many( {"mssql_commands.mssql_command":{'$eq':[]}}, {'$unset': {"mssql_commands":0}} )
            Conn().db.embedded.update_many( {"mssql_fingerprints.mssql_fingerprint":{'$eq':[]}}, {'$unset': {"mssql_fingerprints":0}} ) 
            Conn().db.embedded.update_many( {"mysql_details":{'$eq':[]}}, {'$unset': {"mysql_details":0}} )
            break
        
        jeda = time.time() - mulai
        # Menghitung waktu yang diperlukan untuk memproses data
        print(datetime.now())
        text = 'Waktu eksekusi : %s detik' % timedelta(seconds=round(jeda))
        pprint(text) 
        print("")
        # Ketika data sudah masuk, maka diberi jeda selama sekian detik, agar perulangan While tidak berjalan terus menerus
        time.sleep(10)

while True:
    updateData.insertUpdateData()
