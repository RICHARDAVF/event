import { useNavigation } from "@react-navigation/native";
import { useContext } from "react";
import { TouchableOpacity,Text,StyleSheet,View} from "react-native";
import { Contex } from "../../screen/context";

export const EventItemClient = ({id,nombre,apellido,ruc,razon_social,direccion})=>{
    const navigation = useNavigation()
    const globalContex =useContext(Contex);
    const {setClient} = globalContex;
    const selectCliente = (datos)=>{
        setClient(datos)
        navigation.navigate('Lista')
    }
    
    return (
       
        <TouchableOpacity style={styles.card} onPress={()=>selectCliente({nombre:nombre,apellido:apellido,ruc:ruc,razon_social:razon_social,direccion:direccion})} >
            <View style={styles.container}>
            <View style={styles.column}>
                <Text>ID: {id}</Text>
                <Text>Nombre: {nombre}</Text>
                <Text>Apellido: {apellido}</Text>
            </View>
            <View style={styles.column}>
                <Text>RUC: {ruc}</Text>
                <Text>Razon S.: {razon_social}</Text>
                <Text>Direccion: {direccion}</Text>
            </View>
            </View>
        </TouchableOpacity>
    );
}

const styles = StyleSheet.create({
    card:{
        borderWidth:1,
        borderColor:'gray',
        borderRadius:10,
        marginVertical:5,
        padding:30,
        
    },
    container: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        paddingVertical: 10,
      },
    column: {
        flex: 1,}
});