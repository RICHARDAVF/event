import { View,TextInput,StyleSheet } from "react-native";
import { EventListClient } from "../../components/events/event-list-client";
import { useNavigation } from "@react-navigation/native";
import { useEffect, useState } from "react";
import { TouchableOpacity } from "react-native";
import { Ionicons } from "@expo/vector-icons";

export const Cliente = ()=>{
    const navigation = useNavigation();
    const [data,setData] = useState([]);
    useEffect(()=>{
        fetchData();
    },[])
    const fetchData= async ()=>{
        const res = await fetch('http://192.168.1.110:8000/api/usuarios/',{
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