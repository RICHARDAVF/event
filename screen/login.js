import React,{ useState,useContext, useEffect} from "react";
import { StatusBar } from "expo-status-bar";
import { StyleSheet, View, Text, TextInput, TouchableOpacity, Alert } from "react-native";
import { Contex } from "./context";
import AsyncStorage from '@react-native-async-storage/async-storage';



export const Login = ({action}) => {
    const globalContex = useContext(Contex)
    const {ruc,setRuc,usuario,setUsuario} = globalContex;
    const [password, setPassword] = useState('');
    useEffect(() => {
        checkIfLoggedIn();
      }, []);
    
      const checkIfLoggedIn = async () => {
        try {
          const value = await AsyncStorage.getItem("token");
        
          if (value !== null) {
            const { user, ruc } = JSON.parse(value);
            action();
            setRuc(ruc)
            setUsuario(user)
           
          }
        } catch (error) {
          console.log("Error retrieving token from AsyncStorage", error);
        }
      };
    const handleLogin = async () => {
       
        try{ 
            const res = await fetch(`http://192.168.1.110:8000/api/client/login/${ruc}/${usuario}/${password}/`, {
                method: 'GET',
            });
            console.log(res)
            const data = await res.json({ruc,usuario})
            if (data.usuario===undefined){
                Alert.alert(
                    'Usuario o Contraseña incorrecta',
                    'Por favor, intente de nuevo',
                );
            }
            else{
                const dataAsyn = {
                    user : data.usuario,
                    ruc : data.ruc,
                }
                await AsyncStorage.setItem("token", JSON.stringify(dataAsyn));
                action();
                setUsuario(data.usuario)
            }
            
        }catch(error){
           
            Alert.alert('Complete Todos los campos')
        }
        
    }
   

    return (
        <View style={styles.container}>
            <Text style={styles.titulo}>Hello</Text>
            <Text style={styles.subtitle}>Login</Text>
            <TextInput style={styles.txtinput}
                placeholder="RUC"
                value={ruc}
                onChangeText={setRuc}
            />
            <TextInput style={styles.txtinput}
                value={usuario}
                onChangeText={setUsuario}
                placeholder="USUARIO"
            />
            <TextInput style={styles.txtinput}
                value={password}
                onChangeText={setPassword}
                placeholder="CONTRASEÑA"
                secureTextEntry={true}
               
                
            />
            
            <StatusBar style="auto" />
            <TouchableOpacity style={styles.btnlogin} onPress={handleLogin}>
                <Text style={{ fontSize: 30 }}>Iniciar Sesion</Text>
            </TouchableOpacity>
        </View>
    );
}


const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: "#fff",
        alignItems: "center",
        justifyContent: "center",
    },
    titulo: {
        fontSize: 50,
        fontWeight: "bold",
        marginBottom: 20,
    },
    subtitle: {
        fontSize: 25,
        marginBottom: 50,
    },
    txtinput: {
        height: 50,
        width:'80%',
        borderWidth: 2,
        borderRadius: 30,
        paddingLeft: 20,
        marginBottom: 20,
    },
    btnlogin: {
        marginTop: 30,
        backgroundColor: "cyan",
        borderRadius: 30,
        width:'80%',
        padding:10,
        alignItems:'center'
    },
    
});
