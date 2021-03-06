# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
import pulumi_aws

__all__ = ['UserArgs', 'User']

@pulumi.input_type
class UserArgs:
    def __init__(__self__, *,
                 create_iam_access_key: pulumi.Input[bool],
                 create_user_login_profile: pulumi.Input[bool],
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 password_length: Optional[pulumi.Input[float]] = None,
                 password_reset_required: Optional[pulumi.Input[bool]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 permissions_boundary: Optional[pulumi.Input[str]] = None,
                 pgp_key: Optional[pulumi.Input[str]] = None,
                 ssh_key_encoding: Optional[pulumi.Input[str]] = None,
                 ssh_public_key: Optional[pulumi.Input[str]] = None,
                 upload_iam_user_ssh_key: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a User resource.
        :param pulumi.Input[bool] create_iam_access_key: Boolean to determine whether to create an IAM access key
        :param pulumi.Input[bool] create_user_login_profile: Boolean to determine whether to create an IAM user login profile
        """
        pulumi.set(__self__, "create_iam_access_key", create_iam_access_key)
        pulumi.set(__self__, "create_user_login_profile", create_user_login_profile)
        if force_destroy is not None:
            pulumi.set(__self__, "force_destroy", force_destroy)
        if password_length is not None:
            pulumi.set(__self__, "password_length", password_length)
        if password_reset_required is not None:
            pulumi.set(__self__, "password_reset_required", password_reset_required)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if permissions_boundary is not None:
            pulumi.set(__self__, "permissions_boundary", permissions_boundary)
        if pgp_key is not None:
            pulumi.set(__self__, "pgp_key", pgp_key)
        if ssh_key_encoding is not None:
            pulumi.set(__self__, "ssh_key_encoding", ssh_key_encoding)
        if ssh_public_key is not None:
            pulumi.set(__self__, "ssh_public_key", ssh_public_key)
        if upload_iam_user_ssh_key is not None:
            pulumi.set(__self__, "upload_iam_user_ssh_key", upload_iam_user_ssh_key)

    @property
    @pulumi.getter(name="createIamAccessKey")
    def create_iam_access_key(self) -> pulumi.Input[bool]:
        """
        Boolean to determine whether to create an IAM access key
        """
        return pulumi.get(self, "create_iam_access_key")

    @create_iam_access_key.setter
    def create_iam_access_key(self, value: pulumi.Input[bool]):
        pulumi.set(self, "create_iam_access_key", value)

    @property
    @pulumi.getter(name="createUserLoginProfile")
    def create_user_login_profile(self) -> pulumi.Input[bool]:
        """
        Boolean to determine whether to create an IAM user login profile
        """
        return pulumi.get(self, "create_user_login_profile")

    @create_user_login_profile.setter
    def create_user_login_profile(self, value: pulumi.Input[bool]):
        pulumi.set(self, "create_user_login_profile", value)

    @property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "force_destroy")

    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_destroy", value)

    @property
    @pulumi.getter(name="passwordLength")
    def password_length(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "password_length")

    @password_length.setter
    def password_length(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "password_length", value)

    @property
    @pulumi.getter(name="passwordResetRequired")
    def password_reset_required(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "password_reset_required")

    @password_reset_required.setter
    def password_reset_required(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "password_reset_required", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter(name="permissionsBoundary")
    def permissions_boundary(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "permissions_boundary")

    @permissions_boundary.setter
    def permissions_boundary(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "permissions_boundary", value)

    @property
    @pulumi.getter(name="pgpKey")
    def pgp_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "pgp_key")

    @pgp_key.setter
    def pgp_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pgp_key", value)

    @property
    @pulumi.getter(name="sshKeyEncoding")
    def ssh_key_encoding(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ssh_key_encoding")

    @ssh_key_encoding.setter
    def ssh_key_encoding(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssh_key_encoding", value)

    @property
    @pulumi.getter(name="sshPublicKey")
    def ssh_public_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ssh_public_key")

    @ssh_public_key.setter
    def ssh_public_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssh_public_key", value)

    @property
    @pulumi.getter(name="uploadIamUserSshKey")
    def upload_iam_user_ssh_key(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "upload_iam_user_ssh_key")

    @upload_iam_user_ssh_key.setter
    def upload_iam_user_ssh_key(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "upload_iam_user_ssh_key", value)


class User(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_iam_access_key: Optional[pulumi.Input[bool]] = None,
                 create_user_login_profile: Optional[pulumi.Input[bool]] = None,
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 password_length: Optional[pulumi.Input[float]] = None,
                 password_reset_required: Optional[pulumi.Input[bool]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 permissions_boundary: Optional[pulumi.Input[str]] = None,
                 pgp_key: Optional[pulumi.Input[str]] = None,
                 ssh_key_encoding: Optional[pulumi.Input[str]] = None,
                 ssh_public_key: Optional[pulumi.Input[str]] = None,
                 upload_iam_user_ssh_key: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Create a User resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] create_iam_access_key: Boolean to determine whether to create an IAM access key
        :param pulumi.Input[bool] create_user_login_profile: Boolean to determine whether to create an IAM user login profile
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a User resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param UserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_iam_access_key: Optional[pulumi.Input[bool]] = None,
                 create_user_login_profile: Optional[pulumi.Input[bool]] = None,
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 password_length: Optional[pulumi.Input[float]] = None,
                 password_reset_required: Optional[pulumi.Input[bool]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 permissions_boundary: Optional[pulumi.Input[str]] = None,
                 pgp_key: Optional[pulumi.Input[str]] = None,
                 ssh_key_encoding: Optional[pulumi.Input[str]] = None,
                 ssh_public_key: Optional[pulumi.Input[str]] = None,
                 upload_iam_user_ssh_key: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserArgs.__new__(UserArgs)

            if create_iam_access_key is None and not opts.urn:
                raise TypeError("Missing required property 'create_iam_access_key'")
            __props__.__dict__["create_iam_access_key"] = create_iam_access_key
            if create_user_login_profile is None and not opts.urn:
                raise TypeError("Missing required property 'create_user_login_profile'")
            __props__.__dict__["create_user_login_profile"] = create_user_login_profile
            __props__.__dict__["force_destroy"] = force_destroy
            __props__.__dict__["password_length"] = password_length
            __props__.__dict__["password_reset_required"] = password_reset_required
            __props__.__dict__["path"] = path
            __props__.__dict__["permissions_boundary"] = permissions_boundary
            __props__.__dict__["pgp_key"] = pgp_key
            __props__.__dict__["ssh_key_encoding"] = ssh_key_encoding
            __props__.__dict__["ssh_public_key"] = ssh_public_key
            __props__.__dict__["upload_iam_user_ssh_key"] = upload_iam_user_ssh_key
            __props__.__dict__["access_key"] = None
            __props__.__dict__["iam_user"] = None
            __props__.__dict__["ssh_key"] = None
            __props__.__dict__["user_login_profile"] = None
        super(User, __self__).__init__(
            'awsIam:index:User',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> pulumi.Output[Optional['pulumi_aws.iam.AccessKey']]:
        """
        The access key associated with the IAM user
        """
        return pulumi.get(self, "access_key")

    @property
    @pulumi.getter(name="iamUser")
    def iam_user(self) -> pulumi.Output['pulumi_aws.iam.User']:
        """
        The IAM user
        """
        return pulumi.get(self, "iam_user")

    @property
    @pulumi.getter(name="sshKey")
    def ssh_key(self) -> pulumi.Output[Optional['pulumi_aws.iam.SshKey']]:
        """
        The SSH key associated with the IAM user
        """
        return pulumi.get(self, "ssh_key")

    @property
    @pulumi.getter(name="userLoginProfile")
    def user_login_profile(self) -> pulumi.Output[Optional['pulumi_aws.iam.UserLoginProfile']]:
        """
        The user login profile associated with the IAM user
        """
        return pulumi.get(self, "user_login_profile")

