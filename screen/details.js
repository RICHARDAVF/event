import  {useNavigation, useRoute} from '@react-navigation/native'
import { useLayoutEffect, useState } from 'react';
import { TextInput } from 'react-native';
import { View,StyleSheet ,Text,TouchableOpacity} from "react-native";


export const Detail =() => {
    const route = useRoute();
    const navigation  = useNavigation();
    const {data} = route.params;
    const [cantidad,setCantidad] = useState('1');
    useLayoutEffect(()=>{
        navigation.setOptions({
            headerTitle:'Producto Seleccionado',
            headerTitleAlign:'center'
            
            
        })
    },[])
    return(
        <View style={styles.home}>
            <Text>Elemento seleccionado 1</Text>
            <View  style={{flexDirection:'row' ,justifyContent:'space-between'}} >
                <Text style={styles.txt} >Producto: </Text>
                <TextInput style={styles.txtinput} editable={false}  value={data[1]}/>
            </View>
            <View  style={{flexDirection:'row' ,justifyContent:'space-between'}} >
                <Text style={styles.txt}>Descripcion: </Text>
                <TextInput style={styles.txtinput} value={data[2]}/>
            </View>
            <View style={{flexDirection:'row' ,justifyContent:'space-between'}} >
                <Text style={styles.txt}>Precio</Text>
                <TextInput style={styles.txtinput} value={data[3]}/>
            </View>
            <View style={{flexDirection:'row' ,justifyContent:'space-between'}} >
                <Text style={styles.txt}>Cantidad</Text>
                <TextInput style={styles.txtinput}  value={cantidad} onChangeText={setCantidad}/>
            </View>
            <View style={{flexDirection:'row' ,justifyContent:'space-between'}} >
                <Text style={styles.txt}>Descuento</Text>
                <TextInput style={styles.txtinput}  value={data[5]} editable={true}/>
            </View>
            <View style={{flexDirection:'row' ,justifyContent:'space-between'}} >
                <Text style={styles.txt}>Total s/</Text>
                <Text  style={styles.txt}>S/ {(data[3]*parseFloat(cantidad))?(data[3]*parseFloat(cantidad))-parseFloat(cantidad)*data[5]/100:0}</Text>
            </View>
            <TouchableOpacity style={styles.btn}>
                <Text style={{fontSize:20}}>Agregrar</Text>
            </TouchableOpacity>
        </View>
    )
    
}
const styles = StyleSheet.create({
    home:{
        padding:20,
        fontSize:30,

    },
    txt:{
        fontSize:22,
        color:'#000'
    },
    txtinput:{
        fontSize:22,
        borderWidth:1,
        paddingTop:10,
        marginTop:10,
        width:"50%",
        textAlign:'center',
        marginLeft:12,
        textShadowColor:'#000'
        
    },
    btn:{
        width:'100%',
        backgroundColor:'#abcdef',
        height:30,
        justifyContent:'center',
        alignItems:'center',
        borderRadius:15,
        marginTop:10
    }
})