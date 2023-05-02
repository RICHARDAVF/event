import { View,StyleSheet, Button} from "react-native";
import { EventList } from "../components/events/event-list-product";
import { useEffect, useState } from "react";
import  { useRoute} from '@react-navigation/native'

export const Lista=()=>{
    const [data,setData] = useState([])
  
    useEffect(()=>{
        fetchData()
    },[])
    const fetchData = async () => {
        const res = await fetch('http://192.168.0.104:8000/api/client/');
        const data = await res.json();
        setData(data)
    }

    const handleRefresh = () => {
        fetchData();
    }
      
    return(
        <View style={styles.list}>
            <Button title="Refresh" onPress={handleRefresh} />
            <EventList data={data} />
        </View>
    );
    
}
const styles = StyleSheet.create({
    list:{
        padding:20
    }
})
