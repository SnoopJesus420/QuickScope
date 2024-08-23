import argparse
import ipaddress

# Convert IP to integer
def ip_to_int(ip):
    try:
        return int(ipaddress.ip_address(ip))
    except ValueError:
        raise ValueError(f"Invalid IP address: {ip}")

# Convert integer to IP
def int_to_ip(ip_int):
    return str(ipaddress.ip_address(ip_int))

# Generate IP range list
def generate_ip_list(start_ip, end_ip):
    start_int = ip_to_int(start_ip)
    end_int = ip_to_int(end_ip)
    
    if start_int > end_int:
        raise ValueError("Start IP should be less than or equal to End IP.")
    
    return [int_to_ip(ip) for ip in range(start_int, end_int + 1)]

# Write IP list to a text file
def write_to_file(ip_list, filename):
    try:
        with open(filename, "w") as file:
            for ip in ip_list:
                file.write(ip + "\n")
        print(f"IP list written to {filename}")
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")

# Filter out IPs in the exception list
def filter_exceptions(ip_list, exceptions):
    # Convert exceptions to a set for faster lookups
    exceptions_set = set(exceptions)
    return [ip for ip in ip_list if ip not in exceptions_set]

# Read IPs from a file
def read_exceptions_from_file(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Warning: Exception file {filename} not found.")
        return []
    except IOError as e:
        print(f"Error reading file {filename}: {e}")
        return []

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def main():
    # Setup command line argument parser
    parser = argparse.ArgumentParser(
        description="Generate a list of IP addresses in a given range and save it to a text file.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        "-s", "--start-ip",
        required=True,
        help="The starting IP address of the range."
    )
    
    parser.add_argument(
        "-e", "--end-ip",
        required=True,
        help="The ending IP address of the range."
    )
    
    parser.add_argument(
        "-o", "--output",
        default="ip_list.txt",
        help="The output text file where the IP list will be saved."
    )
    
    parser.add_argument(
        "-x", "--exceptions",
        nargs='*',
        help="A list of IP addresses to exclude from the output, or a file containing IPs to exclude."
    )
    
    args = parser.parse_args()

    # Validate start and end IP addresses
    if not validate_ip(args.start_ip):
        print(f"Invalid start IP address: {args.start_ip}")
        return
    if not validate_ip(args.end_ip):
        print(f"Invalid end IP address: {args.end_ip}")
        return

    # Generate the list of IP addresses
    try:
        ip_list = generate_ip_list(args.start_ip, args.end_ip)
    except ValueError as ve:
        print(ve)
        return
    
    # Process exceptions if provided
    exceptions = []
    if args.exceptions:
        for item in args.exceptions:
            # If the item is a valid file, read the IPs from the file
            try:
                with open(item, 'r') as file:
                    exceptions.extend([line.strip() for line in file if line.strip()])
            except FileNotFoundError:
                # Otherwise, treat it as a manually typed IP address
                if validate_ip(item):
                    exceptions.append(item)
                else:
                    print(f"Invalid IP address in exceptions: {item}")
    
    # Remove duplicates in exceptions
    exceptions = list(set(exceptions))

    # Filter out exceptions from the IP list
    if exceptions:
        ip_list = filter_exceptions(ip_list, exceptions)
    
    # Write the list to the specified output file
    write_to_file(ip_list, args.output)

if __name__ == "__main__":
    main()
