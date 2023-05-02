import { useEffect, useState } from "react";
import { View ,Text} from "react-native";
import { EventListProduc } from "../../components/events/event-list-product";
import { StyleSheet } from "react-native";

import { TouchableOpacity } from "react-native";
import { Ionicons, MaterialCommunityIcons } from '@expo/vector-icons';
export const ListaProducto = ()=>{
    const [data,setData] = useState([])
  
    useEffect(()=>{
        fetchData()
    },[])
    const fetchData = async () => {
        const res = await fetch('http://192.168.0.104:8000/api/product/',{
            method:'GET',
        });
        const dates = await res.json();
        setData(dates)
    }

    const handleRefresh = () => {
        fetchData();
    }
    return (
        <View style={{flex:1}}>
            <View style = {styles.panelClient}>
                <Text style={{fontSize:20,padding:10,color:'#000'}}>CLiente:</Text>
                <Text style={{fontSize:20,padding:10,color:'#000'}}>SIMOLAI S.A.C</Text>
                <TouchableOpacity style={{backgroundColor:'cyan',height:30,marginTop:10, alignItems:'center',borderRadius:12}}>
                    <Text style={{fontSize:20}}>Agregar Cliente  <MaterialCommunityIcons name="face-man" size={22} color="black" /></Text>
                   
                </TouchableOpacity>
                
            </View>
            {/* <Button title="Refresh" onPress={handleRefresh} /> */}
            
            <EventListProduc data={data} action = {handleRefresh}/>
        
        </View>
    );
}
const styles = StyleSheet.create({
    panelClient:{
        width:"100%",
        height:'10%',
        backgroundColor:'#e8f3ff',
        flexDirection:'row'
        

    }
});