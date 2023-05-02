import { useEffect, useState, useContext} from "react";
import { View ,Text} from "react-native";
import { EventListProduc } from "../../components/events/event-list-product";
import { StyleSheet } from "react-native";
import { TouchableOpacity } from "react-native";
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { useNavigation } from "@react-navigation/native";
import { Contex } from "../../screen/context";
export const ListaProducto = ()=>{
    const globalContex = useContext(Contex)
    const navigation  = useNavigation()
    const [data,setData] = useState([])
    const {client} = globalContex;
    const [product,setProduct] = useState([]);
    console.log(client.nombre)
    useEffect(()=>{
        fetchData()
    },[])
    const fetchData = async () => {
        const res = await fetch('http://192.168.1.110:8000/api/product/',{
            method:'GET',
        });
        
        const dates = await res.json();
        setData(dates)
    }

   
    return (
        <View style={{flex:1}}>
            <View style = {styles.panelClient}>
                <Text style={{fontSize:20,padding:10,color:'#000'}}>Cliente:</Text>
                <Text style={{fontSize:20,padding:10,color:'#000'}}>{("nombre" in client)?client.nombre+' '+client.apellido:''}</Text>
                <TouchableOpacity style={{backgroundColor:'cyan',height:30,marginTop:10, alignItems:'center',borderRadius:12}} onPress={()=>navigation.navigate('Cliente')} >
                    <Text style={{fontSize:20}}>{("nombre" in client)?"Cambiar":"Agregar"}<MaterialCommunityIcons name="face-man" size={22} color="black" /></Text>
                   
                </TouchableOpacity> 
            </View>
            <View style={{paddingLeft:15}}>
                <Text>{("ruc" in client)?"RUC: "+client.ruc:''}</Text>
                <Text>{("razon_social" in client)?"Razon Social: "+client.razon_social:''}</Text>
                <Text>{("direccion" in client)?"Dirrecion: "+client.direccion:''}</Text>
            </View>
            <EventListProduc data={data} />
        
        </View>
    );
}
const styles = StyleSheet.create({
    panelClient:{
        width:"100%",
        backgroundColor:'#e8f3ff',
        flexDirection:'row',
        borderWidth:1,
        

    }
});