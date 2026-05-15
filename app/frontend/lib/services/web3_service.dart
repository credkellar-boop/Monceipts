import 'package:http/http.dart';
import 'package:web3dart/web3dart.dart';

class Web3Service {
  final String rpcUrl = "https://rpc-devnet.monad.xyz";
  late Web3Client _client;

  Web3Service() {
    _client = Web3Client(rpcUrl, Client());
  }

  // Get balance of a MON account
  Future<EtherAmount> getBalance(String address) async {
    return await _client.getBalance(EthereumAddress.fromHex(address));
  }

  // Send MON (Native Token Transfer)
  Future<String> sendMon({
    required String privateKey,
    required String receiverAddress,
    required double amount,
  }) async {
    final credentials = EthPrivateKey.fromHex(privateKey);
    
    return await _client.sendTransaction(
      credentials,
      Transaction(
        to: EthereumAddress.fromHex(receiverAddress),
        value: EtherAmount.fromUnitAndValue(EtherUnit.ether, (amount * 1e18).toInt()),
      ),
      chainId: 10143, // Monad Devnet ID
    );
  }

  // Check transaction status
  Future<TransactionReceipt?> getReceipt(String txHash) async {
    return await _client.getTransactionReceipt(txHash);
  }
}
