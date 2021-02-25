function formatDate(userDate) {
    // format from M/D/YYYY to YYYYMMDD
    var date = userDate.split('/')
    if (Number(date[1]) < 10 ) {
        date[1] = '0'+ date[1]
    }
    if (Number(date[0]) < 10 ) {
        date[0] = '0'+ date[0]
    }
    return date[2]+date[0]+date[1]
  }
  
  console.log(formatDate("1/1/2014"));