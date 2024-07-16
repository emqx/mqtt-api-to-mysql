
const store = {
  index: 0
}

function generator(faker, options) {
  const clientid = options.clientId

  function generateTempData() {
    const device_id = clientid; // 设备
    const temperature = faker.datatype.float({ min: 20.0, max: 100.0 }); // 温度，单位：摄氏度
    const humidity = faker.datatype.float({ min: 0.0, max: 100.0 }); // 湿度

    return {
      device_id,
      temperature,
      humidity
    };
  }

  if (!store[clientid]) {
    store[clientid] = {
      id: faker.datatype.uuid(),
      name: `temp_data_${store.index}`,
    }
    store.index += 1
  }

  const data = store[clientid]
  const message = { ...generateTempData(), ...data, }
  return {
    message: JSON.stringify(message),
  }
}


const name = 'temp-data'
const author = 'EMQX Team'
const dataFormat = 'JSON'
const version = '0.0.1'
const description = 'Temp data generator'

module.exports = {
  generator,
  name,
  author,
  dataFormat,
  version,
  description,
}

