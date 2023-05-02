
import React, { useEffect, useState } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { NavigationContainer } from '@react-navigation/native';
import { MyDrawer } from './navigation/drawer';
import { StatusBar } from 'expo-status-bar';
import { Login } from './screen/login';
import { Provider } from "./screen/context";

const App = () => {


  const [showFirstView, setShowFirstView] = useState(true);
  const handleButtonPress = () => {
    setShowFirstView(false);
  };

  const checkIfLoggedIn = async () => {
    try {
      const value = await AsyncStorage.getItem("token");
      console.log(value)
      if (value !== null) {
        setShowFirstView(false)
        

      }
    } catch (error) {
      console.log("Error retrieving token from AsyncStorage", error);
    }
  useEffect(() => {
      checkIfLoggedIn();
    }, []);
  };
  return (

    <Provider>

      <NavigationContainer>
        {showFirstView ? (
          <Login action={handleButtonPress} />

        ) : (
          <>
            <MyDrawer status={setShowFirstView} />
            <StatusBar style='light' />
          </>
        )}
        <StatusBar style='auto' />
      </NavigationContainer>


    </Provider>
  );
};

export default App;