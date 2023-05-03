
import { View ,Text,StyleSheet} from "react-native";
import { useContext } from "react";
import { Contex } from "./context";
import { DUMMY_DATA } from "../data/dummy";
export const QrCodeScreen = ()=>{
    const globalContex = useContext(Contex)
    
    const iterData = DUMMY_DATA.map((value,index)=>(
        <View key={index}>
            <Text>{value.title}</Text>
            <Text>{value.descripcion}</Text>
        </View>
    ))

    
    return(
        <View style={styles.scren}>
            {iterData}
            
        </View>
    );

}
const styles = StyleSheet.create({
    scren:{
        padding:20
    }
});