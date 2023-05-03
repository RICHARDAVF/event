import { View,TextInput,StyleSheet } from "react-native";
import { EventListClient } from "../../components/events/event-list-client";
import { useContext, useEffect, useState } from "react";
import { TouchableOpacity } from "react-native";
import { Ionicons } from "@expo/vector-icons";
import { Contex } from "../context";

export const EventListVenta = (data)=>{
    const renderItem =({item})=>{
        
    }
    const globalContex= useContext(Contex)
    const {dominio} = globalContex;
    console.log(dominio)
    const [data,setData] = useState([]);
    useEffect(()=>{
        fetchData();
    },[])
    const fetchData= async ()=>{
        const res = await fetch(`${dominio}:8000/api/usuarios/`,{
            method:'GET'
        }) ;
        const dates = await res.json();
        setData(dates)
    }
    return(
        <View style={{flex:1}}>
            <View style={styles.panelClient}>
                <TextInput placeholder="Buscar Cliente" style={{paddingRight:20,borderBottomWidth:1,width:'50%'}}/>
                <TouchableOpacity style={{paddingRight:20}}>
                    <Ionicons name="search" size={30}/>
                </TouchableOpacity>
            </View>
            <EventListClient data ={data} />
        </View>
    );

} 
const styles = StyleSheet.create({
    panelClient:{
        width:"100%",
        backgroundColor:'#e8f3ff',
        flexDirection:'row',
        alignItems:'flex-end',
        alignContent:'flex-end',
        justifyContent:'flex-end',
        

    }
});