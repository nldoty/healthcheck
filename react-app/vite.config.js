import path from 'path';
import { resolve } from 'path'

export default {
  root: path.resolve(__dirname, 'src'),
  resolve: {
    alias: {
      '~coreui': resolve(__dirname, 'node_modules/@coreui/coreui'),
      // for CoreUI PRO users
      // '~coreui': resolve(__dirname, 'node_modules/@coreui/coreui-pro'),
    }
  },
  server: {
    port: 8080,
    hot: true
  }
}