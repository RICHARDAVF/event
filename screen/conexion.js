
import MSSQL from 'react-native-mssql'


// export default function conexion() {
// const sql = require('mssql')
//   useEffect(() => {
//     const config = {
//       user: 'sa',
//       password: 'Noi2011',
//       server: '192.168.1.37',
//       database: 'siia_arauco',
//       port: 1433,
//     };
    
//     const executeQuery = async () => {
//       try {
//         const pool = await sql.connect(config);
//         const result = await pool.request().query('SELECT * FROM t_usuario');
//         console.log(result.recordset);
//       } catch (err) {
//         console.error(err);
//       }
//     };

//     executeQuery();
//   }, []);

  

// }
export default function con(){
  const config = {
    server: '192.168.1.37',
    username: 'sa',
    password: 'Noi2011',
    database: 'siia_arauco',
    port: 1433,
  };

  MSSQL.connect(config)
    .then(() => {
      console.log('Connection Successful!');
    })
    .catch((error) => {
      console.log('Error:', error);
    });

}